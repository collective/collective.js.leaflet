default_profile = 'profile-collective.js.leaflet:default'


def upgrade_10_to_11(context):
    context.runImportStepFromProfile(default_profile, 'cssregistry')


def upgrade_11_to_12(context):
    context.runImportStepFromProfile(default_profile, 'cssregistry')


def upgrade_12_to_13(context):
    context.runImportStepFromProfile(default_profile, 'cssregistry')
    context.runImportStepFromProfile(default_profile, 'jsregistry')


def upgrade_13_to_14(context):
    context.runImportStepFromProfile(default_profile, 'cssregistry')
