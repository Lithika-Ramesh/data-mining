"""
Environment Check Script for GMM Analysis
Run this script to verify that all dependencies are installed correctly.

Usage:
    python check_environment.py
"""

import sys
import importlib
from pathlib import Path

def check_python_version():
    """Check if Python version is 3.7 or higher"""
    version = sys.version_info
    print(f"[OK] Python version: {version.major}.{version.minor}.{version.micro}")
    if version.major < 3 or (version.major == 3 and version.minor < 7):
        print("  [WARN] Python 3.7+ recommended")
        return False
    return True

def check_package(package_name, display_name=None):
    """Check if a package is installed"""
    if display_name is None:
        display_name = package_name
    
    try:
        module = importlib.import_module(package_name)
        version = getattr(module, '__version__', 'unknown')
        print(f"[OK] {display_name:25s} version: {version}")
        return True
    except ImportError:
        print(f"[FAIL] {display_name:25s} NOT INSTALLED")
        return False

def check_data_files():
    """Check if required data files exist"""
    print("\nChecking data files...")
    
    data_files = [
        '../data/features_unsupervised.csv',
        '../data/features_supervised.csv'
    ]
    
    all_exist = True
    for file_path in data_files:
        path = Path(file_path)
        if path.exists():
            size_mb = path.stat().st_size / (1024 * 1024)
            print(f"[OK] {file_path:40s} ({size_mb:.2f} MB)")
        else:
            print(f"[FAIL] {file_path:40s} NOT FOUND")
            all_exist = False
    
    return all_exist

def check_reports_directory():
    """Check if reports directory exists"""
    reports_dir = Path('../reports')
    if not reports_dir.exists():
        print(f"\n[WARN] Creating '../reports/' directory...")
        reports_dir.mkdir(parents=True, exist_ok=True)
        print(f"[OK] '../reports/' directory created")
    else:
        print(f"\n[OK] '../reports/' directory exists")
    return True

def main():
    """Main environment check"""
    print("="*70)
    print("GMM UNSUPERVISED LEARNING - ENVIRONMENT CHECK")
    print("="*70)
    
    print("\nChecking Python version...")
    python_ok = check_python_version()
    
    print("\nChecking required packages...")
    packages = [
        ('numpy', 'NumPy'),
        ('pandas', 'Pandas'),
        ('sklearn', 'scikit-learn'),
        ('matplotlib', 'Matplotlib'),
        ('seaborn', 'Seaborn'),
        ('plotly', 'Plotly'),
        ('scipy', 'SciPy'),
        ('IPython', 'IPython'),
    ]
    
    packages_ok = all(check_package(pkg, name) for pkg, name in packages)
    
    print("\nChecking optional packages...")
    optional_packages = [
        ('jupyterlab', 'JupyterLab'),
        ('joblib', 'joblib'),
    ]
    
    for pkg, name in optional_packages:
        check_package(pkg, name)
    
    data_ok = check_data_files()
    reports_ok = check_reports_directory()
    
    print("\n" + "="*70)
    print("SUMMARY")
    print("="*70)
    
    if python_ok and packages_ok and data_ok and reports_ok:
        print("\n[SUCCESS] All checks passed! You're ready to run the GMM analysis.")
        print("\nNext steps:")
        print("  1. Open Jupyter: jupyter notebook unsupervised_gmm.ipynb")
        print("  2. Run all cells: Kernel -> Restart & Run All")
        print("  3. Wait for completion (5-15 minutes)")
        print("  4. Check reports/ directory for outputs")
    else:
        print("\n[WARNING] Some checks failed. Please address the issues above.")
        
        if not packages_ok:
            print("\nTo install missing packages:")
            print("  pip install -r requirements_gmm.txt")
        
        if not data_ok:
            print("\nData files are missing. Please ensure:")
            print("  - ../data/features_unsupervised.csv exists")
            print("  - You're running this script from the gmm_analysis/ directory")
    
    print("\n" + "="*70)

if __name__ == "__main__":
    main()
