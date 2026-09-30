## com.apple.accessoryd.matching

> `/System/Library/UserEventPlugins/com.apple.accessoryd.matching.plugin/com.apple.accessoryd.matching`

```diff

-1139.40.6.0.0
-  __TEXT.__text: 0x3b984
+1139.60.9.0.0
+  __TEXT.__text: 0x3c094
   __TEXT.__auth_stubs: 0x1000
-  __TEXT.__objc_stubs: 0x4e00
-  __TEXT.__objc_methlist: 0x237c
-  __TEXT.__cstring: 0x4994
-  __TEXT.__objc_methname: 0x6da0
+  __TEXT.__objc_stubs: 0x5040
+  __TEXT.__objc_methlist: 0x23ac
+  __TEXT.__cstring: 0x4d8b
+  __TEXT.__objc_methname: 0x6eb0
   __TEXT.__objc_classname: 0x2b5
   __TEXT.__objc_methtype: 0xada
-  __TEXT.__const: 0x218
-  __TEXT.__oslogstring: 0x3f3e
-  __TEXT.__gcc_except_tab: 0x550
+  __TEXT.__const: 0x228
+  __TEXT.__oslogstring: 0x3f81
+  __TEXT.__gcc_except_tab: 0x554
   __TEXT.__ustring: 0x18
   __TEXT.__unwind_info: 0x9f0
   __DATA.__auth_got: 0x810
-  __DATA.__got: 0x340
+  __DATA.__got: 0x358
   __DATA.__auth_ptr: 0x18
-  __DATA.__const: 0x1030
-  __DATA.__cfstring: 0x36a0
+  __DATA.__const: 0x1070
+  __DATA.__cfstring: 0x3940
   __DATA.__objc_classlist: 0xb0
   __DATA.__objc_catlist: 0x10
   __DATA.__objc_protolist: 0x48
   __DATA.__objc_imageinfo: 0x8
-  __DATA.__objc_const: 0x3c80
-  __DATA.__objc_selrefs: 0x19c0
+  __DATA.__objc_const: 0x3cb0
+  __DATA.__objc_selrefs: 0x1a20
   __DATA.__objc_protorefs: 0x8
   __DATA.__objc_superrefs: 0xa8
-  __DATA.__objc_ivar: 0x388
+  __DATA.__objc_ivar: 0x38c
   __DATA.__objc_data: 0x6e0
   __DATA.__objc_arraydata: 0xe8
   __DATA.__objc_arrayobj: 0x90

   __DATA.__common: 0x18
   - /System/Library/Frameworks/AudioToolbox.framework/AudioToolbox
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
+  - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/Frameworks/Security.framework/Security

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: 188CF395-3E55-3EE8-8826-75441DF8471B
-  Functions: 1423
-  Symbols:   8168
-  CStrings:  2917
+  UUID: 12089E58-C8C8-3DC8-9AF8-0A8B703E0CF3
+  Functions: 1428
+  Symbols:   8220
+  CStrings:  2976
 
Symbols:
+ +[accessorydMatchingPlugin launchTTRForPort:]
+ -[ACCUserNotification alternateButtonName]
+ -[ACCUserNotification setAlternateButtonName:]
+ GCC_except_table261
+ GCC_except_table69
+ GCC_except_table82
+ OBJC_IVAR_$_ACCUserNotification._alternateButtonName
+ _OBJC_CLASS_$_LSApplicationWorkspace
+ _OBJC_CLASS_$_NSURLComponents
+ _OBJC_CLASS_$_NSURLQueryItem
+ __45+[accessorydMatchingPlugin launchTTRForPort:]_block_invoke.cold.1
+ __55-[accessorydMatchingPlugin addUserNotificationForPort:]_block_invoke.395
+ __55-[accessorydMatchingPlugin addUserNotificationForPort:]_block_invoke.396
+ __55-[accessorydMatchingPlugin addUserNotificationForPort:]_block_invoke.396.cold.1
+ __55-[accessorydMatchingPlugin addUserNotificationForPort:]_block_invoke.397
+ __55-[accessorydMatchingPlugin addUserNotificationForPort:]_block_invoke.397.cold.1
+ __55-[accessorydMatchingPlugin addUserNotificationForPort:]_block_invoke.397.cold.2
+ __55-[accessorydMatchingPlugin addUserNotificationForPort:]_block_invoke.397.cold.3
+ __55-[accessorydMatchingPlugin addUserNotificationForPort:]_block_invoke.402
+ __55-[accessorydMatchingPlugin addUserNotificationForPort:]_block_invoke.405
+ __55-[accessorydMatchingPlugin addUserNotificationForPort:]_block_invoke.405.cold.1
+ __55-[accessorydMatchingPlugin addUserNotificationForPort:]_block_invoke.405.cold.2
+ __55-[accessorydMatchingPlugin addUserNotificationForPort:]_block_invoke.405.cold.3
+ __55-[accessorydMatchingPlugin addUserNotificationForPort:]_block_invoke.405.cold.4
+ __55-[accessorydMatchingPlugin addUserNotificationForPort:]_block_invoke_2.399
+ __55-[accessorydMatchingPlugin addUserNotificationForPort:]_block_invoke_2.399.cold.1
+ __55-[accessorydMatchingPlugin addUserNotificationForPort:]_block_invoke_2.399.cold.2
+ __55-[accessorydMatchingPlugin addUserNotificationForPort:]_block_invoke_2.403
+ __55-[accessorydMatchingPlugin addUserNotificationForPort:]_block_invoke_2.403.cold.1
+ __IOAccessoryManagerEventCallback_block_invoke.960
+ __IOAccessoryManagerEventCallback_block_invoke.960.cold.1
+ __IOAccessoryManagerEventCallback_block_invoke.961
+ __IOAccessoryManagerEventCallback_block_invoke.961.cold.1
+ __IOAccessoryManagerEventCallback_block_invoke.962
+ __IOAccessoryManagerEventCallback_block_invoke.963
+ __IOAccessoryManagerEventCallback_block_invoke.965
+ __OBJC_$_CLASS_METHODS_accessorydMatchingPlugin
+ ___45+[accessorydMatchingPlugin launchTTRForPort:]_block_invoke
+ ___block_descriptor_32_e34_v24?0"NSDictionary"8"NSError"16l
+ ___block_descriptor_48_e8_32s40s_e8_v12?0i8ls32l8s40l8
+ __block_literal_global.1001
+ __block_literal_global.1004
+ __block_literal_global.1006
+ __block_literal_global.1009
+ __block_literal_global.1021
+ __block_literal_global.1023
+ __block_literal_global.326
+ __block_literal_global.329
+ __block_literal_global.401
+ __block_literal_global.972
+ __block_literal_global.981
+ __serviceLDCMMitigationStatusChanged_block_invoke.1002
+ __serviceLDCMMitigationStatusChanged_block_invoke.1002.cold.1
+ __serviceLDCMMitigationStatusChanged_block_invoke.1002.cold.2
+ __serviceLDCMMitigationStatusChanged_block_invoke.1002.cold.3
+ __serviceLDCMMitigationStatusChanged_block_invoke.1002.cold.4
+ _objc_msgSend$URL
+ _objc_msgSend$alternateButtonName
+ _objc_msgSend$builtIn
+ _objc_msgSend$bundleIdentifier
+ _objc_msgSend$connectionActive
+ _objc_msgSend$connectionUUID
+ _objc_msgSend$defaultWorkspace
+ _objc_msgSend$launchTTRForPort:
+ _objc_msgSend$mainBundle
+ _objc_msgSend$openURL:configuration:completionHandler:
+ _objc_msgSend$portNumber
+ _objc_msgSend$portType
+ _objc_msgSend$portTypeDescription
+ _objc_msgSend$queryItemWithName:value:
+ _objc_msgSend$setAlternateButtonName:
+ _objc_msgSend$setHost:
+ _objc_msgSend$setQueryItems:
+ _objc_msgSend$setScheme:
- GCC_except_table259
- GCC_except_table65
- GCC_except_table80
- __55-[accessorydMatchingPlugin addUserNotificationForPort:]_block_invoke.308
- __55-[accessorydMatchingPlugin addUserNotificationForPort:]_block_invoke.309
- __55-[accessorydMatchingPlugin addUserNotificationForPort:]_block_invoke.309.cold.1
- __55-[accessorydMatchingPlugin addUserNotificationForPort:]_block_invoke.312
- __55-[accessorydMatchingPlugin addUserNotificationForPort:]_block_invoke.312.cold.1
- __55-[accessorydMatchingPlugin addUserNotificationForPort:]_block_invoke.312.cold.2
- __55-[accessorydMatchingPlugin addUserNotificationForPort:]_block_invoke.312.cold.3
- __55-[accessorydMatchingPlugin addUserNotificationForPort:]_block_invoke.317
- __55-[accessorydMatchingPlugin addUserNotificationForPort:]_block_invoke.320
- __55-[accessorydMatchingPlugin addUserNotificationForPort:]_block_invoke.320.cold.1
- __55-[accessorydMatchingPlugin addUserNotificationForPort:]_block_invoke.320.cold.2
- __55-[accessorydMatchingPlugin addUserNotificationForPort:]_block_invoke.320.cold.3
- __55-[accessorydMatchingPlugin addUserNotificationForPort:]_block_invoke.320.cold.4
- __55-[accessorydMatchingPlugin addUserNotificationForPort:]_block_invoke_2.314
- __55-[accessorydMatchingPlugin addUserNotificationForPort:]_block_invoke_2.314.cold.1
- __55-[accessorydMatchingPlugin addUserNotificationForPort:]_block_invoke_2.314.cold.2
- __55-[accessorydMatchingPlugin addUserNotificationForPort:]_block_invoke_2.318
- __55-[accessorydMatchingPlugin addUserNotificationForPort:]_block_invoke_2.318.cold.1
- __IOAccessoryManagerEventCallback_block_invoke.874
- __IOAccessoryManagerEventCallback_block_invoke.874.cold.1
- __IOAccessoryManagerEventCallback_block_invoke.875
- __IOAccessoryManagerEventCallback_block_invoke.875.cold.1
- __IOAccessoryManagerEventCallback_block_invoke.876
- __IOAccessoryManagerEventCallback_block_invoke.877
- __IOAccessoryManagerEventCallback_block_invoke.879
- ___block_descriptor_40_e8_32s_e8_v12?0i8ls32l8
- __block_literal_global.241
- __block_literal_global.316
- __block_literal_global.886
- __block_literal_global.895
- __block_literal_global.915
- __block_literal_global.918
- __block_literal_global.920
- __block_literal_global.923
- __block_literal_global.935
- __block_literal_global.937
- __serviceLDCMMitigationStatusChanged_block_invoke.916
- __serviceLDCMMitigationStatusChanged_block_invoke.916.cold.1
- __serviceLDCMMitigationStatusChanged_block_invoke.916.cold.2
- __serviceLDCMMitigationStatusChanged_block_invoke.916.cold.3
- __serviceLDCMMitigationStatusChanged_block_invoke.916.cold.4
CStrings:
+ "1"
+ "1660904"
+ "2129482"
+ "BundleID"
+ "ComponentID"
+ "ComponentName"
+ "ComponentVersion"
+ "Description"
+ "Error launching radar! (error: %@)"
+ "File Radar"
+ "IncludeDevicePrefixInTitle"
+ "Keywords"
+ "Launching TTR... (radarURL: %@)"
+ "New Bugs"
+ "T@\"NSString\",C,N,V_alternateButtonName"
+ "TimeOfIssue"
+ "Title"
+ "Transport Restricted Mode (TRM)"
+ "Transport Restricted Mode (TRM) Issue Report\nFiled via Tap-to-Radar Button\n\nISSUE DESCRIPTION:\nWhat happened?\n\nEXPECTED BEHAVIOR:\nWhat did you expect to happen?\n\nACTUAL BEHAVIOR:\nWhat actually happened instead?\n\nSTEPS TO REPRODUCE:\n1. \n2. \n3. \n\nADDITIONAL DETAILS:\nAny other relevant information...\n\n\n\n[AUTO-GENERATED TRM CONTEXT - DO NOT MODIFY BELOW]\n\n*** Port Info ***\nportDescription: %@\nportType: %d\nportTypeDescription: %@\nportNumber: %d\nbuiltIn: %s\nconnectionActive: %s\nconnectionUUID: %@\n\n*** Port Authorization State ***\nauthorizationRequired: %s\nauthorizationPending: %s\nuserAuthorizationPending: %s\ntransportsUnauthorized: %@\nuserAuthorizationStatus: %d\nuserAuthorizationStatusDescription: %@\n\nTimestamp: %@\n\n\n"
+ "URL"
+ "[TTR] [TRM] "
+ "_alternateButtonName"
+ "alternateButtonName"
+ "bundleIdentifier"
+ "defaultWorkspace"
+ "launchTTRForPort:"
+ "mainBundle"
+ "new"
+ "openURL:configuration:completionHandler:"
+ "queryItemWithName:value:"
+ "setAlternateButtonName:"
+ "setHost:"
+ "setQueryItems:"
+ "setScheme:"
+ "tap-to-radar"
+ "v24@?0@\"NSDictionary\"8@\"NSError\"16"
+ "yyyy-MM-dd HH:mm:ss"
+ "yyyy.MM.dd_HH-mm-ss"

```
