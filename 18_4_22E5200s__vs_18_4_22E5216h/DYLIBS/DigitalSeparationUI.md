## DigitalSeparationUI

> `/System/Library/PrivateFrameworks/DigitalSeparationUI.framework/DigitalSeparationUI`

```diff

-425.0.98.0.0
-  __TEXT.__text: 0x3b420
-  __TEXT.__auth_stubs: 0x880
-  __TEXT.__objc_methlist: 0x47e8
+425.0.106.0.0
+  __TEXT.__text: 0x3cc24
+  __TEXT.__auth_stubs: 0x870
+  __TEXT.__objc_methlist: 0x49c8
+  __TEXT.__cstring: 0x3b51
   __TEXT.__const: 0x116
-  __TEXT.__cstring: 0x3b11
   __TEXT.__gcc_except_tab: 0x4d8
-  __TEXT.__oslogstring: 0x1d29
+  __TEXT.__oslogstring: 0x1e22
   __TEXT.__dlopen_cstrs: 0x15e
   __TEXT.__swift5_typeref: 0x68
   __TEXT.__constg_swiftt: 0x8c

   __TEXT.__swift5_types: 0x8
   __TEXT.__swift_as_entry: 0x14
   __TEXT.__swift_as_ret: 0x14
-  __TEXT.__unwind_info: 0xee8
+  __TEXT.__unwind_info: 0xf00
   __TEXT.__eh_frame: 0x168
-  __TEXT.__objc_classname: 0x875
-  __TEXT.__objc_methname: 0xc569
+  __TEXT.__objc_classname: 0x889
+  __TEXT.__objc_methname: 0xcae9
   __TEXT.__objc_methtype: 0x26dc
-  __TEXT.__objc_stubs: 0x8ce0
-  __DATA_CONST.__got: 0x718
-  __DATA_CONST.__const: 0xdf0
-  __DATA_CONST.__objc_classlist: 0x198
+  __TEXT.__objc_stubs: 0x90c0
+  __DATA_CONST.__got: 0x728
+  __DATA_CONST.__const: 0xe58
+  __DATA_CONST.__objc_classlist: 0x1a0
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0xe8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2f48
+  __DATA_CONST.__objc_selrefs: 0x3040
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0x168
+  __DATA_CONST.__objc_superrefs: 0x170
   __DATA_CONST.__objc_arraydata: 0xa0
-  __AUTH_CONST.__auth_got: 0x450
+  __AUTH_CONST.__auth_got: 0x448
   __AUTH_CONST.__auth_ptr: 0x10
   __AUTH_CONST.__const: 0x5c0
-  __AUTH_CONST.__cfstring: 0x42a0
-  __AUTH_CONST.__objc_const: 0xf170
+  __AUTH_CONST.__cfstring: 0x4320
+  __AUTH_CONST.__objc_const: 0xf3c0
   __AUTH_CONST.__objc_dictobj: 0xf0
   __AUTH_CONST.__objc_intobj: 0x1f8
-  __AUTH.__objc_data: 0x1008
+  __AUTH.__objc_data: 0x1058
   __AUTH.__data: 0xc0
-  __DATA.__objc_ivar: 0x3c8
+  __DATA.__objc_ivar: 0x3ec
   __DATA.__data: 0xb40
-  __DATA.__bss: 0x258
+  __DATA.__bss: 0x268
   __DATA.__common: 0x1f8
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/Contacts.framework/Contacts

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 1586
-  Symbols:   1968
-  CStrings:  3027
+  Functions: 1625
+  Symbols:   2019
+  CStrings:  3087
 
Symbols:
+ _DSDescriptorKeyErrorDisabledKey
+ _DSDescriptorKeyErrorUninstalledKey
+ _DSDescriptorKeyErrorUnlaunchedKey
+ _DSDescriptorKeyFetchErrorKey
+ _DSDescriptorKeyMultipleAppsKey
+ _DSDescriptorKeySingleAppKey
+ _DSDescriptorKeyStopSharingErrorKey
+ _DSDescriptorKeyTitleKey
+ _DSSourceErrorDomain
+ _OBJC_CLASS_$_DSErrorDescriptor
+ _OBJC_METACLASS_$_DSErrorDescriptor
- _dispatch_sync
CStrings:
+ "\x06"
+ "\n"
+ "DSErrorDescriptor"
+ "DSLogWifiSyncDetail"
+ "ERROR_APP_UNINSTALLED"
+ "Error occured when removing computer from detail controller: %@"
+ "Error occurred during data fetch: %@"
+ "Error occurred when attempting to remove selected devices: %@"
+ "Failed to fetch paired devices with error %@"
+ "T@\"NSArray\",&,N,V_errors"
+ "T@\"NSArray\",&,N,V_localizedAppNames"
+ "T@\"NSArray\",&,N,V_presentableLocalizedAppNames"
+ "T@\"NSDictionary\",&,N,V_presentableErrorsByLocalizedAppName"
+ "T@\"NSMutableArray\",&,N,V_resetErrors"
+ "T@\"NSString\",&,N,V_localizedMessage"
+ "T@\"NSString\",&,N,V_localizedTitle"
+ "TB,N,V_shouldShowRatchetPlatter"
+ "TB,N,V_showRatchetPlatter"
+ "TITLE"
+ "User confirmed disconnect for device: %@"
+ "WITH_APP_NAME"
+ "WITH_MULTIPLE_APPS"
+ "_"
+ "_describeErrorsWithKey:"
+ "_errors"
+ "_localizedAppNames"
+ "_localizedMessage"
+ "_localizedTitle"
+ "_presentableErrorsByLocalizedAppName"
+ "_presentableLocalizedAppNames"
+ "_resetErrors"
+ "_shouldShowRatchetPlatter"
+ "_showRatchetPlatter"
+ "ds_alertControllerWithResetErrors:"
+ "ds_localizedAppNamesByPresentableError"
+ "errors"
+ "initWithFetchSharingError:"
+ "initWithStopSharingErrors:"
+ "localizedAppNames"
+ "localizedMessage"
+ "localizedTitle"
+ "multipleNameMessageFormatForError:"
+ "multipleSourceErrorFormatWithDSErrorType:sourceErrorType:"
+ "namelessTitleForError:"
+ "presentableErrorsByLocalizedAppName"
+ "presentableLocalizedAppNames"
+ "presentableSourceErrors:"
+ "resetErrors"
+ "setErrors:"
+ "setLocalizedAppNames:"
+ "setLocalizedMessage:"
+ "setLocalizedTitle:"
+ "setObject:forKey:"
+ "setPresentableErrorsByLocalizedAppName:"
+ "setPresentableLocalizedAppNames:"
+ "setResetErrors:"
+ "setShouldShowRatchetPlatter:"
+ "setShowRatchetPlatter:"
+ "setUpAppNamesAndErrorDict"
+ "shouldShowPlatterForRatchetState:"
+ "shouldShowRatchetPlatter"
+ "showRatchetPlatter"
+ "singleNameMessageFormatForError:"
+ "singleNameTitleFormatForError:"
+ "singleSourceErrorFormatWithDSErrorType:sourceErrorType:"
+ "startEmergencyResetWithPresentingViewController:showRatchetWarning:"
+ "startManageSharingWithPresentingViewController:showRatchetWarning:"
- "%@\n\n%@"
- "ERROR_UNINSTALLED_IN_APPSTORE"
- "T@\"NSError\",&,N,V_resetError"
- "_resetError"
- "ds_presentableErrorsByLocalizedAppName"
- "resetError"
- "setResetError:"
- "viewWillLayoutSubviews"

```
