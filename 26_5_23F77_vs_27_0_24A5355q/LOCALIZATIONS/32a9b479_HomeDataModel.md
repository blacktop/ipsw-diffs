## HomeDataModel

> `FileSystem/System/Library/PrivateFrameworks/HomeDataModel.framework/HFLocalizable.loctable`

```diff

 en.HFAccessoriesWithIssuesTitle.accessories.NSStringFormatValueTypeKey = "lu"
 en.HFAccessoriesWithIssuesTitle.accessories.one = "%lu Issue"
 en.HFAccessoriesWithIssuesTitle.accessories.other = "%lu Issues"
+en.HFAccessoryControl_AutoLockPausedUntilDoorClosed = "Auto-lock paused until\ndoor is closed"
 en.HFAccessoryDetailsContainedServicesTitle = "Accessories"
 en.HFAccessoryDetailsCreateRoom = "Create New"
 en.HFAccessoryDetailsCreateRoomBarTitle = "Add Room"

 en.HFCameraStreamingUserAccessLevelStream = "Stream Only"
 en.HFCameraStreamingUserAccessLevelStreamAndViewRecordings = "Stream \u0026 View Recordings"
 en.HFCameraToday = "Today"
+en.HFCameraToday_Day_Time_Format = "%1$@, %2$@"
 en.HFCameraUserAccessModeDescriptionDetectActivity = "This camera is in “Detect Activity” mode and cannot stream or record."
 en.HFCameraUserAccessModeDescriptionManualShutOff = "This camera has been disabled."
 en.HFCameraUserAccessModeDescriptionOff = "This camera is in “Off” mode and cannot stream or record."

 en.HFCharacteristicTitleSmokeDetected = "Smoke Detected"
 en.HFCharacteristicTitleSmokeDetectedSimple = "Smoke Detected"
 en.HFCharacteristicTitleTemperature = "Temperature"
+en.HFCharacteristicTitleTemperatureUnits = "Unit"
 en.HFCharacteristicTriggerDescriptionFormatString = "%1$@ %2$@"
 en.HFCharacteristicTriggerDescriptionFormatString_fullSentence = "When %1$@ %2$@"
 en.HFCharacteristicTriggerDescriptionFormatString_fullSentence_WithAction = "When %1$@ %2$@, %3$@"

 en.HFError_HFOperationTurnOnService_withName_title = "Could not turn on “%@”"
 en.HFError_HFOperationUnlockService_title = "Could not unlock accessory"
 en.HFError_HFOperationUnlockService_withName_title = "Could not unlock “%@”"
-en.HFError_HFOperationUpdateApplicationDataCloudSync_HMErrorCodeOperationTimedOut_description = "Make sure you’re connected to the internet and try again."
-en.HFError_HFOperationUpdateApplicationDataCloudSync_title = "Could not change settings"
+en.HFError_HFOperationUpdateApplicationDataCloudSync_HMErrorCodeOperationTimedOut_description = "Your settings were not updated because your iPhone and home hub are not communicating. As a first step, make sure your home hub is powered on and connected to the same network as your iPhone."
+en.HFError_HFOperationUpdateApplicationDataCloudSync_title = "Unable to Communicate with Home Hub"
 en.HFError_HFOperationUpdateApplicationDataResidentSync_HMErrorCodeOperationTimedOut_description = "Make sure your home hubs are connected to the internet and powered on, then try again."
 en.HFError_HFOperationUpdateApplicationDataResidentSync_title = "Could not change settings"
 en.HFError_HFOperationUpdatePINCode_title = "Could Not Update Access Code"

 en.HFMediaCodexRootGeneralAnalyticsFooter = "Help Apple improve its products and services by automatically sending daily diagnostic and usage data. Data may include location information. "
 en.HFMediaCodexRootGeneralAnalyticsFooter_LinkString = "About Analytics \u0026 Privacy…"
 en.HFMediaCodexRootGeneralAnalyticsFooter_isAMac_LinkString = "Help Apple improve its products and services by automatically sending daily diagnostic and usage data. Data may include location information. About Analytics \u0026 Privacy…\n\nYou can change this setting or view analytics data in Privacy settings on an iPhone or iPad."
+en.HFMediaCodexRootGeneralAnalyticsFooter_settingsDisclosure = "\n\nAnalytics logs for your HomePod are available in Analytics \u0026 Improvements in the Settings app."
+en.HFMediaCodexRootGeneralAnalyticsFooter_settingsDisclosureSettingOff = "\n\nAnalytics logs for your HomePod are available in Analytics \u0026 Improvements in the Settings app. You are not currently sharing daily diagnostic and usage data for HomePod with Apple."
 en.HFMediaCodexRootMusicHeader = "Music \u0026 Podcasts"
 en.HFMediaCodexRootSiriFooter = "Siri can recognize your voice on Home accessories when you make requests."
 en.HFMediaCodexRootSiriHeader = "Siri"

 en.HFServiceDetailsPairingModeItem_Alert_Dismiss = "Dismiss"
 en.HFServiceDetailsPairingModeItem_Alert_Title = "Accessory Ready to Connect"
 en.HFServiceDetailsRemoveAccessoryWithServiceAlertTitle = "Removing “%1$@” will also remove “%2$@” HomePod. Are you sure you want to remove them from your home?"
+en.HFServiceDetailsRemoveBridgeFooter = "Removing this bridge will remove all accessories connected to this bridge."
+en.HFServiceDetailsRemoveBridgeName = "Remove Bridge from Home"
 en.HFServiceDetailsRemoveCameraWithClipsAlertTitle = "If you remove this camera, all recordings associated with this camera will also be deleted from iCloud. Are you sure you want to remove “%@” from your home?"
 en.HFServiceDetailsRemoveDeviceAlertCancelButton = "Cancel"
 en.HFServiceDetailsRemoveDeviceAlertRemoveCameraButton = "Remove Camera"

 en.MatterCommandError-RVC-ServiceArea-SkipArea-InvalidInMode-Description_NoName = "Your vacuum is unable to skip this room."
 en.MatterCommandError-RVC-ServiceArea-SkipArea-InvalidInMode-Title = "Unable to Skip Area"
 en.MatterCommandError-RVC-ServiceArea-UnknownError-Description = "There was an error while trying to change the selected rooms. You can try again or try restarting the vacuum."
+en.MatterCommandError-RVC-UnknownError-Description = "There was an error while Accessory was trying to clean. You can try the cleaning session again or restarting the vacuum."
 en.MatterCommandError-RVC-WaterTankLidOpen-Description = "%@ can start cleaning after the water tank is closed."
 en.MatterCommandError-RVC-WaterTankLidOpen-Description_NoName = "Your vacuum can start cleaning after the water tank is closed."
 en.MatterCommandError-RVC-WaterTankLidOpen-Title = "Close Water Tank"

 en.MatterCommandError-TimeoutError-Description_WLAN = "%@ is not responding. Make sure the vacuum is powered on and connected to WLAN."
 en.MatterCommandError-TimeoutError-Title = "%@ Not Responding"
 en.MatterCommandError-TimeoutError-Title_NoName = "Not Responding"
-en.MatterCommandError-UnknownError-Description = "There was an error while Accessory was trying to clean. You can try the cleaning session again or restarting the vacuum."
+en.MatterCommandError-UnknownError-Description = "There was an error trying to perform the requested action. You can try again or try restarting the accessory."
 en.MatterCommandError-UnknownError-Title = "Unknown Error"
 en.Metrics = "Metrics"
 en.SecuritySystemEventGenericAccessoryName = "Security System"

```
