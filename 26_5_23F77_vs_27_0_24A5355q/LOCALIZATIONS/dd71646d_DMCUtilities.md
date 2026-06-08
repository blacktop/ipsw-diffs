## DMCUtilities

> `FileSystem/System/Library/PrivateFrameworks/DMCUtilities.framework/DMCLocalizable.loctable`

```diff

 en.DMC_ENROLLMENT_PASSCODE_REQUIRED = "Device passcode is required to complete enrollment"
 en.DMC_ENROLLMENT_UPDATE_FROM_FACTORY_VERSION_REQUIRED = "Update from factory version is required to complete enrollment"
 en.DMC_ENTERPRISE_APPLICATION_EXISTS_%@ = "The Enrollment SSO application “%@” has been installed on the device."
+en.DMC_ERROR_MULTI_USER_DIRECT_USER_SWITCH_REQUIRES_NO_USERS = "Authenticated Guest Mode can only be enabled when there’s no user on the device."
+en.DMC_ERROR_MULTI_USER_PROVISIONING_FAILED = "Failed to provision Shared iPad."
+en.DMC_ERROR_MULTI_USER_TEMPORARY_SESSION_ONLY_PERSISTENCE_FAILED = "Failed to persist Shared iPad temporary session only flag."
 en.DMC_INVALID_CLOUD_CONFIG = "The cloud configuration profile is invalid."
 en.DMC_INVALID_ERSSO_DECLARATIONS = "The Enrollment SSO declarations are invalid"
 en.DMC_MAA_SIGN_IN_FAILED = "Failed to sign-in to the Managed Apple Account."

 en.ERROR_PROFILE_MISSING_BOOTSTRAP_TOKEN_CAPABILITY = "The MDM profile does not contain bootstrap token capability"
 en.ERROR_PROFILE_NO_INTERACTIVE_INSTALLATION = "The profile must be installed using a device management tool."
 en.GO_BACK = "Go Back"
+en.HOUR_1_MDM_FINDMY_LOCATION_SENT_TO_%@_%@_%@ = "The location of this device was sent to %@ at %@ on %@."
 en.HTTP_ERROR_403_RESPONSE_FROM_SERVER_NO_MESSAGE_%@ = "The MDM server responded with this error code:\n%@"
 en.HTTP_ERROR_403_RESPONSE_FROM_SERVER_WITH_MESSAGE_%@ = "The MDM server responded with this error message:\n%@"
 en.HTTP_ERROR_403_RESPONSE_PAIRING_TOKEN_MISSING_%@ = "The MDM server requires the pairing token with error message: “%@”."

 en.MDM_ERROR_COULD_NOT_VALIDATE_MEDIA_ID = "The iTunes Store ID of the item could not be validated."
 en.MDM_ERROR_DECLARATIVE_MANAGEMENT_ERROR = "The MDM DeclarativeManagement command failed."
 en.MDM_ERROR_DEVICE_NOT_IN_MDM_LOST_MODE = "The device is not in MDM Lost Mode."
+en.MDM_ERROR_ENHANCED_LOGGING_CONFIGURATION_FAILED = "The Enhanced Logging session could not be configured."
+en.MDM_ERROR_ENHANCED_LOGGING_NOT_SUPPORTED = "Enhanced Logging is not supported on this device."
 en.MDM_ERROR_FETCH_GLOBAL_RESTRICTIONS_FAILED = "Fetching global restrictions failed."
 en.MDM_ERROR_FETCH_PROFILE_RESTRICTIONS_FAILED = "Fetching profile restrictions failed."
 en.MDM_ERROR_FETCH_VID_SEED_FAILED = "An internal error occurred fetching the VID seed."
 en.MDM_ERROR_INVALID_MEDIA_REPLACEMENT_TYPE = "The item must be replaced by a file of the same type."
 en.MDM_ERROR_INVALID_REDEMPTION_CODE = "The redemption code is invalid."
+en.MDM_ERROR_INVALID_REQUEST_MISSING_APPLECARE_TOKEN = "The AppleCare token is required for enhanced log collection."
 en.MDM_ERROR_INVALID_REQUEST_TYPE_IN_MDM_LOST_MODE_P_REQUEST_%@ = "“%@” is not a valid request type while device is in MDM Lost Mode."
 en.MDM_ERROR_INVALID_REQUEST_TYPE_IN_SINGLE_APP_MODE_P_REQUEST_%@ = "“%@” is not a valid request type while this device is in Single App Mode."
 en.MDM_ERROR_INVALID_REQUEST_TYPE_P_REQUEST_%@ = "“%@” is not a valid request type."

 en.MDM_ERROR_SHARED_DEVICE_HAS_EXISTING_USERS = "The user quota / number of resident users cannot be updated if there are existing users on the device."
 en.MDM_ERROR_SHARED_DEVICE_INVALID_QUOTA_SIZE = "The quota size is invalid. Minimum value is 2048"
 en.MDM_ERROR_SHARED_DEVICE_INVALID_RESIDENT_USER_NUMBER = "The number of users must be larger than 0"
+en.MDM_ERROR_SHARED_DEVICE_USER_SESSION_CONFIGURATION_FAILED = "Failed to configure Shared iPad user session settings. Please try again."
 en.MDM_ERROR_SPECIFIED_PROFILE_NOT_INSTALLED_P_ID_%@ = "The profile “%@” is not installed."
 en.MDM_ERROR_SPECIFIED_USER_DOES_NOT_EXIST = "The specified user does not exist on this device."
 en.MDM_ERROR_SPECIFIED_USER_HAS_DATA_TO_SYNC = "The specified user has data to sync."

```
