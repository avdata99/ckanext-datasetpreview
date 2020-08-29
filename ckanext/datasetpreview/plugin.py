import os
import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit


class DatasetpreviewPlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.ITemplateHelpers)
    
    # IConfigurer
    def update_config(self, config_):
        toolkit.add_template_directory(config_, 'templates')
        toolkit.add_public_directory(config_, 'public')
        toolkit.add_resource('fanstatic', 'datasetpreview')

        # define a cache folder for CSV
        storage_path = config_.get('ckan.storage_path')
        cache_folder = os.path.join(storage_path, 'data_preview_cache')
        if not os.path.isdir(cache_folder):
            os.mkdir(cache_folder)
        config_['dataset_preview_cache_path'] = cache_folder

    def configure(self, config):
        self.config = config

    ## ITemplateHelpers
    def get_helpers(self):
        from ckanext.datasetpreview import helpers as dsp_helpers
        return {
            'package_preview': dsp_helpers.package_preview,
            'get_preview_chart_data': dsp_helpers.get_preview_chart_data
        }