from plugins import scan_plugins  # or whatever your loader script is called

def run():
    # Set up the necessary environment
    # This will depend on your specific project
    # ...

    # Load the plugins
    plugins = scan_plugins()

    # Find the plugin that provides the read_emails function
    # This will depend on how your plugin system is designed
    for plugin in plugins:
        if hasattr(plugin, 'read_emails'):
            # Call the function
            plugin.read_emails()

if __name__ == "__main__":
    run()
