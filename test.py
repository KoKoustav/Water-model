import pkg_resources

def get_package_version(package_name):
    try:
        return pkg_resources.get_distribution(package_name).version
    except pkg_resources.DistributionNotFound:
        return None

# Example usage:
print(get_package_version("scikit-learn"))
print(get_package_version("numpy"))
print(get_package_version("pandas"))
print(get_package_version("matplotlib"))


