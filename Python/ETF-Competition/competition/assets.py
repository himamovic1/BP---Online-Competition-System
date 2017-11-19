from flask_assets import Bundle, Environment

css_bundle = Bundle(
    'plugins/bootstrap/css/bootstrap.min.css',
    'plugins/font-awesome/css/font-awesome.min.css',
    'plugins/bootstrap-datetimepicker/build/css/bootstrap-datetimepicker.css',
    'plugins/bootstrap-daterangepicker/daterangepicker.css',
    'plugins/fullcalendar/fullcalendar.css',
    'plugins/build/css/custom.min.css',
    'css/utils.css',
    'css/style.css',
    filters='cssmin',
    output='build/bundle.css'
)

js_bundle = Bundle(
    'plugins/jquery/jquery.min.js',
    'plugins/bootstrap/js/bootstrap.min.js',
    'plugins/moment/min/moment.min.js',
    'plugins/bootstrap-daterangepicker/daterangepicker.js',
    'plugins/bootstrap-datetimepicker/build/js/bootstrap-datetimepicker.min.js',
    'plugins/fullcalendar/fullcalendar.js',
    'plugins/build/js/custom.min.js',
    filters='jsmin',
    output='build/bundle.js'
)

# Environment need to be instantiated in run_app
assets = Environment()

assets.register('css_bundle', css_bundle)
assets.register('js_bundle', js_bundle)
