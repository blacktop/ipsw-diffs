## MobileStoreDemoSetupUI

> `/System/Library/PrivateFrameworks/MobileStoreDemoSetupUI.framework/MobileStoreDemoSetupUI`

```diff

-1254.80.3.0.0
-  __TEXT.__text: 0x140f4
-  __TEXT.__auth_stubs: 0x510
-  __TEXT.__objc_methlist: 0x1278
-  __TEXT.__const: 0xd8
-  __TEXT.__cstring: 0x10ea
+1254.100.45.0.1
+  __TEXT.__text: 0x15d1c
+  __TEXT.__auth_stubs: 0x5a0
+  __TEXT.__objc_methlist: 0x14d8
+  __TEXT.__const: 0xe8
+  __TEXT.__gcc_except_tab: 0x250
+  __TEXT.__cstring: 0x134e
+  __TEXT.__oslogstring: 0xf9b
   __TEXT.__ustring: 0xc
-  __TEXT.__oslogstring: 0xcf7
-  __TEXT.__gcc_except_tab: 0x174
-  __TEXT.__unwind_info: 0x474
-  __TEXT.__objc_classname: 0x49a
-  __TEXT.__objc_methname: 0x5ab5
-  __TEXT.__objc_methtype: 0x19b0
-  __TEXT.__objc_stubs: 0x4280
+  __TEXT.__unwind_info: 0x530
+  __TEXT.__objc_classname: 0x4e4
+  __TEXT.__objc_methname: 0x5f89
+  __TEXT.__objc_methtype: 0x19df
+  __TEXT.__objc_stubs: 0x4740
   __DATA_CONST.__got: 0xc8
-  __DATA_CONST.__const: 0x2d8
-  __DATA_CONST.__objc_classlist: 0xc8
+  __DATA_CONST.__const: 0x328
+  __DATA_CONST.__objc_classlist: 0xe0
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0xa8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x76d8
-  __DATA_CONST.__objc_selrefs: 0x12f8
+  __DATA_CONST.__objc_const: 0x7758
+  __DATA_CONST.__objc_selrefs: 0x1468
+  __DATA_CONST.__objc_classrefs: 0x310
+  __DATA_CONST.__objc_superrefs: 0xb0
   __DATA_CONST.__objc_arraydata: 0x30
-  __AUTH_CONST.__cfstring: 0x1620
-  __AUTH_CONST.__objc_const: 0x8f8
+  __AUTH_CONST.__const: 0x1e0
+  __AUTH_CONST.__cfstring: 0x1720
+  __AUTH_CONST.__objc_const: 0xaa8
   __AUTH_CONST.__objc_doubleobj: 0x30
   __AUTH_CONST.__objc_dictobj: 0x50
-  __AUTH_CONST.__const: 0x160
-  __AUTH_CONST.__auth_got: 0x298
-  __AUTH.__objc_data: 0x7d0
-  __DATA.__objc_classrefs: 0x2e0
-  __DATA.__objc_superrefs: 0xa0
-  __DATA.__objc_ivar: 0x12c
+  __AUTH_CONST.__auth_got: 0x2e0
+  __AUTH.__objc_data: 0x8c0
+  __DATA.__objc_ivar: 0x134
   __DATA.__data: 0x7e0
-  __DATA.__bss: 0x88
+  __DATA.__bss: 0xc8
   - /System/Library/Frameworks/Contacts.framework/Contacts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /System/Library/Frameworks/QuartzCore.framework/QuartzCore
   - /System/Library/Frameworks/UIKit.framework/UIKit
   - /System/Library/PrivateFrameworks/EmbeddedDataReset.framework/EmbeddedDataReset
+  - /System/Library/PrivateFrameworks/IntlPreferences.framework/IntlPreferences
   - /System/Library/PrivateFrameworks/MobileStoreDemoKit.framework/MobileStoreDemoKit
   - /System/Library/PrivateFrameworks/OnBoardingKit.framework/OnBoardingKit
   - /System/Library/PrivateFrameworks/SetupAssistantUI.framework/SetupAssistantUI
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: E0875D4C-D017-3982-8B48-E900B1E180D6
-  Functions: 438
-  Symbols:   2118
-  CStrings:  1636
+  UUID: F731DEEE-7EDE-3F5B-9627-4597F8028008
+  Functions: 498
+  Symbols:   2332
+  CStrings:  1732
 
Symbols:
+ +[MSDLanguageAndRegionHelper sharedInstance]
+ +[MSDLanguageAndRegionManager sharedInstance]
+ +[MSDPreferencesFile preferencesFileExists]
+ +[MSDPreferencesFile preferencesFilePath]
+ +[MSDPreferencesFile preferencesFileUrl]
+ +[MSDPreferencesFile sharedInstance]
+ -[MSDLanguageAndRegionHelper _isCurrentDeviceLanguage:andRegion:]
+ -[MSDLanguageAndRegionHelper _systemLocalizedLanguageCodeFromArray:]
+ -[MSDLanguageAndRegionHelper getCurrentDeviceLanguage]
+ -[MSDLanguageAndRegionHelper getCurrentDevicePreferredLanguage]
+ -[MSDLanguageAndRegionHelper getCurrentDeviceRegion]
+ -[MSDLanguageAndRegionHelper getCurrentLocaleCode]
+ -[MSDLanguageAndRegionHelper setDeviceLanguage:andRegion:]
+ -[MSDLanguageAndRegionManager .cxx_destruct]
+ -[MSDLanguageAndRegionManager cancelNotifyToken:]
+ -[MSDLanguageAndRegionManager deviceLanguageIdentifier]
+ -[MSDLanguageAndRegionManager deviceRegionCode]
+ -[MSDLanguageAndRegionManager getCurrentDeviceLanguage]
+ -[MSDLanguageAndRegionManager getCurrentDeviceLocaleCode]
+ -[MSDLanguageAndRegionManager getCurrentDevicePreferredLanguage]
+ -[MSDLanguageAndRegionManager getCurrentDeviceRegion]
+ -[MSDLanguageAndRegionManager getDemoPreferencesLanguage]
+ -[MSDLanguageAndRegionManager getDemoPreferencesRegion]
+ -[MSDLanguageAndRegionManager init]
+ -[MSDLanguageAndRegionManager queue]
+ -[MSDLanguageAndRegionManager restoreDeviceLanguageAndRegionIfNeeded]
+ -[MSDLanguageAndRegionManager restoreDeviceLanguageAndRegionIfNeeded].cold.1
+ -[MSDLanguageAndRegionManager saveCurrentDeviceLanguageIdentifier]
+ -[MSDLanguageAndRegionManager saveCuurentDeviceRegionCode]
+ -[MSDLanguageAndRegionManager saveDeviceLanguageIdentifier:]
+ -[MSDLanguageAndRegionManager saveDeviceRegionCode:]
+ -[MSDLanguageAndRegionManager setDeviceLanguage:andRegion:sbRestartNeeded:sbRestartHandler:]
+ -[MSDLanguageAndRegionManager setDeviceLanguage:andRegion:sbRestartNeeded:sbRestartHandler:].cold.1
+ -[MSDLanguageAndRegionManager setDeviceLanguage:andRegion:sbRestartNeeded:sbRestartHandler:].cold.2
+ -[MSDLanguageAndRegionManager setQueue:]
+ -[MSDPreferencesFile .cxx_destruct]
+ -[MSDPreferencesFile cache]
+ -[MSDPreferencesFile deepCopy:]
+ -[MSDPreferencesFile init]
+ -[MSDPreferencesFile objectForKey:]
+ -[MSDPreferencesFile objectForKey:].cold.1
+ -[MSDPreferencesFile populateCache]
+ -[MSDPreferencesFile raiseInvalidPropertyListObjectExceptionForObject:]
+ -[MSDPreferencesFile reload]
+ -[MSDPreferencesFile removeObjectForKey:]
+ -[MSDPreferencesFile removeObjectForKey:].cold.1
+ -[MSDPreferencesFile removeObjectsForKeys:]
+ -[MSDPreferencesFile removeObjectsForKeys:].cold.1
+ -[MSDPreferencesFile saveCache]
+ -[MSDPreferencesFile setCache:]
+ -[MSDPreferencesFile setObject:forKey:]
+ GCC_except_table3
+ GCC_except_table5
+ GCC_except_table6
+ GCC_except_table7
+ GCC_except_table9
+ _CFPropertyListCreateDeepCopy
+ _OBJC_CLASS_$_IPSettingsUtilities
+ _OBJC_CLASS_$_MSDLanguageAndRegionHelper
+ _OBJC_CLASS_$_MSDLanguageAndRegionManager
+ _OBJC_CLASS_$_MSDPreferencesFile
+ _OBJC_CLASS_$_NSException
+ _OBJC_CLASS_$_NSPropertyListSerialization
+ _OBJC_IVAR_$_MSDLanguageAndRegionManager._queue
+ _OBJC_IVAR_$_MSDPreferencesFile._cache
+ _OBJC_METACLASS_$_MSDLanguageAndRegionHelper
+ _OBJC_METACLASS_$_MSDLanguageAndRegionManager
+ _OBJC_METACLASS_$_MSDPreferencesFile
+ _OUTLINED_FUNCTION_1
+ __OBJC_$_CLASS_METHODS_MSDLanguageAndRegionHelper
+ __OBJC_$_CLASS_METHODS_MSDLanguageAndRegionManager
+ __OBJC_$_CLASS_METHODS_MSDPreferencesFile
+ __OBJC_$_INSTANCE_METHODS_MSDLanguageAndRegionHelper
+ __OBJC_$_INSTANCE_METHODS_MSDLanguageAndRegionManager
+ __OBJC_$_INSTANCE_METHODS_MSDPreferencesFile
+ __OBJC_$_INSTANCE_VARIABLES_MSDLanguageAndRegionManager
+ __OBJC_$_INSTANCE_VARIABLES_MSDPreferencesFile
+ __OBJC_$_PROP_LIST_MSDLanguageAndRegionManager
+ __OBJC_$_PROP_LIST_MSDPreferencesFile
+ __OBJC_CLASS_RO_$_MSDLanguageAndRegionHelper
+ __OBJC_CLASS_RO_$_MSDLanguageAndRegionManager
+ __OBJC_CLASS_RO_$_MSDPreferencesFile
+ __OBJC_METACLASS_RO_$_MSDLanguageAndRegionHelper
+ __OBJC_METACLASS_RO_$_MSDLanguageAndRegionManager
+ __OBJC_METACLASS_RO_$_MSDPreferencesFile
+ ___36+[MSDPreferencesFile sharedInstance]_block_invoke
+ ___40+[MSDPreferencesFile preferencesFileUrl]_block_invoke
+ ___44+[MSDLanguageAndRegionHelper sharedInstance]_block_invoke
+ ___45+[MSDLanguageAndRegionManager sharedInstance]_block_invoke
+ ___92-[MSDLanguageAndRegionManager setDeviceLanguage:andRegion:sbRestartNeeded:sbRestartHandler:]_block_invoke
+ ___92-[MSDLanguageAndRegionManager setDeviceLanguage:andRegion:sbRestartNeeded:sbRestartHandler:]_block_invoke.4
+ ___block_descriptor_56_e8_32s40bs48r_e5_v8?0lr48l8s32l8s40l8
+ ___block_descriptor_56_e8_32s40bs48r_e8_v12?0i8ls32l8r48l8s40l8
+ ___block_literal_global.12
+ _dispatch_after
+ _kCFAllocatorDefault
+ _notify_cancel
+ _notify_get_state
+ _notify_register_check
+ _notify_register_dispatch
+ _objc_getProperty
+ _objc_msgSend$_isCurrentDeviceLanguage:andRegion:
+ _objc_msgSend$_systemLocalizedLanguageCodeFromArray:
+ _objc_msgSend$cache
+ _objc_msgSend$cancelNotifyToken:
+ _objc_msgSend$deepCopy:
+ _objc_msgSend$deviceLanguageIdentifier
+ _objc_msgSend$deviceRegionCode
+ _objc_msgSend$dictionaryWithContentsOfURL:error:
+ _objc_msgSend$dictionaryWithDictionary:
+ _objc_msgSend$exceptionWithName:reason:userInfo:
+ _objc_msgSend$fileURLWithPath:isDirectory:
+ _objc_msgSend$getCurrentDeviceLanguage
+ _objc_msgSend$getCurrentDevicePreferredLanguage
+ _objc_msgSend$getCurrentDeviceRegion
+ _objc_msgSend$getCurrentLocaleCode
+ _objc_msgSend$path
+ _objc_msgSend$populateCache
+ _objc_msgSend$preferencesFileExists
+ _objc_msgSend$preferencesFilePath
+ _objc_msgSend$preferencesFileUrl
+ _objc_msgSend$preferredLanguages
+ _objc_msgSend$preferredLocalizationsFromArray:forPreferences:
+ _objc_msgSend$propertyList:isValidForFormat:
+ _objc_msgSend$queue
+ _objc_msgSend$raise
+ _objc_msgSend$raiseInvalidPropertyListObjectExceptionForObject:
+ _objc_msgSend$removeObjectForKey:
+ _objc_msgSend$removeObjectsForKeys:
+ _objc_msgSend$saveCache
+ _objc_msgSend$saveDeviceLanguageIdentifier:
+ _objc_msgSend$saveDeviceRegionCode:
+ _objc_msgSend$setCache:
+ _objc_msgSend$setDeviceLanguage:andRegion:
+ _objc_msgSend$setLanguage:
+ _objc_msgSend$setQueue:
+ _objc_msgSend$setRegion:
+ _objc_msgSend$stringByAppendingPathExtension:
+ _objc_msgSend$systemLanguages
+ _objc_msgSend$writeToURL:error:
+ _objc_retain_x25
+ _objc_setProperty_atomic
+ _preferencesFileUrl.fileUrl
+ _preferencesFileUrl.onceToken
- _NSLocaleCountryCode
- _objc_msgSend$languageCode
CStrings:
+ "%@_%@"
+ "%{public}s - Both object and key must be non-nil."
+ "%{public}s - Exception:  %{public}@"
+ "%{public}s - Failed to read preferences file:  %{public}@ - Error:  %{public}@"
+ "%{public}s - Failed to save preferences file:  %{public}@ - Error:  %{public}@"
+ "%{public}s - Key is nil."
+ "%{public}s - Key must be of type NSString."
+ "%{public}s - Keys array pointer is nil."
+ "-[MSDPreferencesFile objectForKey:]"
+ "-[MSDPreferencesFile populateCache]"
+ "-[MSDPreferencesFile raiseInvalidPropertyListObjectExceptionForObject:]"
+ "-[MSDPreferencesFile removeObjectForKey:]"
+ "-[MSDPreferencesFile removeObjectsForKeys:]"
+ "-[MSDPreferencesFile saveCache]"
+ "-[MSDPreferencesFile setObject:forKey:]"
+ "/private/var/mnt/com.apple.mobilestoredemo.storage/com.apple.mobilestoredemo.blob/Metadata"
+ "B48@0:8@16@24^B32@?40"
+ "Deadline for Springboard restart passed."
+ "Device already has language %{public}@ (%{public}@) and region %{public}@"
+ "DeviceLanguageIdentifier"
+ "DeviceRegionCode"
+ "Failed to save device language."
+ "Failed to save device region."
+ "Failed to set device language and region."
+ "InvalidPropertyListObject"
+ "MSDLanguageAndRegionHelper"
+ "MSDLanguageAndRegionManager"
+ "MSDPreferencesFile"
+ "Object %@ of type %@ is not a valid property list object."
+ "Setting device language to %{public}@ (%{public}@) and region code to %{public}@."
+ "Springboard restarted."
+ "T@\"NSMutableDictionary\",&,V_cache"
+ "T@\"NSObject<OS_dispatch_queue>\",&,N,V_queue"
+ "T@\"NSString\",?,C,N"
+ "T@\"NSString\",?,R,C"
+ "T@\"NSString\",?,R,C,N"
+ "T@\"NSString\",?,R,C,N,V_title"
+ "T@\"UITextInputPasswordRules\",?,C,N"
+ "TB,?,N"
+ "TB,?,N,GisSecureTextEntry"
+ "Tq,?,N"
+ "_cache"
+ "_isCurrentDeviceLanguage:andRegion:"
+ "_queue"
+ "_systemLocalizedLanguageCodeFromArray:"
+ "cache"
+ "cancelNotifyToken:"
+ "com.apple.msd_language_and_region"
+ "com.apple.springboard.finishedstartup"
+ "deepCopy:"
+ "deviceLanguageIdentifier"
+ "deviceRegionCode"
+ "dictionaryWithContentsOfURL:error:"
+ "dictionaryWithDictionary:"
+ "exceptionWithName:reason:userInfo:"
+ "fileURLWithPath:isDirectory:"
+ "getCurrentDeviceLanguage"
+ "getCurrentDeviceLocaleCode"
+ "getCurrentDevicePreferredLanguage"
+ "getCurrentDeviceRegion"
+ "getCurrentLocaleCode"
+ "getDemoPreferencesLanguage"
+ "getDemoPreferencesRegion"
+ "i32@0:8@16@24"
+ "path"
+ "plist"
+ "populateCache"
+ "preferencesFileExists"
+ "preferencesFilePath"
+ "preferencesFileUrl"
+ "preferredLanguages"
+ "preferredLocalizationsFromArray:forPreferences:"
+ "propertyList:isValidForFormat:"
+ "queue"
+ "raise"
+ "raiseInvalidPropertyListObjectExceptionForObject:"
+ "reload"
+ "removeObjectForKey:"
+ "removeObjectsForKeys:"
+ "restoreDeviceLanguageAndRegionIfNeeded"
+ "saveCache"
+ "saveCurrentDeviceLanguageIdentifier"
+ "saveCuurentDeviceRegionCode"
+ "saveDeviceLanguageIdentifier:"
+ "saveDeviceRegionCode:"
+ "setCache:"
+ "setDeviceLanguage:andRegion:"
+ "setDeviceLanguage:andRegion:sbRestartNeeded:sbRestartHandler:"
+ "setLanguage:"
+ "setQueue:"
+ "setRegion:"
+ "stringByAppendingPathExtension:"
+ "systemLanguages"
+ "v12@?0i8"
+ "v20@0:8i16"
+ "writeToURL:error:"
- "T@\"NSString\",C,N"
- "T@\"NSString\",R,C,N"
- "T@\"NSString\",R,C,N,V_title"
- "T@\"UITextInputPasswordRules\",C,N"
- "TB,N"
- "TB,N,GisSecureTextEntry"
- "Tq,N"
- "languageCode"

```
