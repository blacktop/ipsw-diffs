## CoreAccessories

> `/System/Library/PrivateFrameworks/CoreAccessories.framework/Versions/A/CoreAccessories`

```diff

-1025.80.3.0.1
-  __TEXT.__text: 0x26c9c
-  __TEXT.__auth_stubs: 0x480
-  __TEXT.__objc_methlist: 0xf98
+1043.100.30.0.0
+  __TEXT.__text: 0x29518
+  __TEXT.__auth_stubs: 0x4f0
+  __TEXT.__objc_methlist: 0x17a4
   __TEXT.__const: 0x158
-  __TEXT.__cstring: 0x37fc
-  __TEXT.__oslogstring: 0x37ec
-  __TEXT.__gcc_except_tab: 0xab4
+  __TEXT.__cstring: 0x38b8
+  __TEXT.__oslogstring: 0x3a6a
+  __TEXT.__gcc_except_tab: 0xacc
   __TEXT.__ustring: 0xa
-  __TEXT.__unwind_info: 0x818
+  __TEXT.__unwind_info: 0x898
   __TEXT.__objc_classname: 0x258
-  __TEXT.__objc_methname: 0x41d4
-  __TEXT.__objc_methtype: 0x140f
-  __TEXT.__objc_stubs: 0x28a0
-  __DATA_CONST.__got: 0x130
+  __TEXT.__objc_methname: 0x43a4
+  __TEXT.__objc_methtype: 0x1524
+  __TEXT.__objc_stubs: 0x29c0
+  __DATA_CONST.__got: 0x140
   __DATA_CONST.__const: 0x14d8
   __DATA_CONST.__objc_classlist: 0x50
   __DATA_CONST.__objc_protolist: 0x68
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xd58
+  __DATA_CONST.__objc_selrefs: 0xe48
   __DATA_CONST.__objc_protorefs: 0x50
   __DATA_CONST.__objc_superrefs: 0x48
   __DATA_CONST.__objc_arraydata: 0xd8
-  __AUTH_CONST.__auth_got: 0x250
-  __AUTH_CONST.__const: 0x1250
-  __AUTH_CONST.__cfstring: 0x35e0
-  __AUTH_CONST.__objc_const: 0x2fe8
+  __AUTH_CONST.__auth_got: 0x288
+  __AUTH_CONST.__const: 0x1370
+  __AUTH_CONST.__cfstring: 0x3620
+  __AUTH_CONST.__objc_const: 0x2258
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH_CONST.__objc_intobj: 0x30
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH.__objc_data: 0x2d0
   __DATA.__objc_ivar: 0xd0
-  __DATA.__data: 0x830
-  __DATA.__bss: 0x100
+  __DATA.__data: 0x838
+  __DATA.__bss: 0x128
   __DATA.__common: 0xc
   __DATA_DIRTY.__objc_data: 0x50
-  __DATA_DIRTY.__data: 0x50
+  __DATA_DIRTY.__data: 0x48
   __DATA_DIRTY.__common: 0xc
-  __DATA_DIRTY.__bss: 0x28
+  __DATA_DIRTY.__bss: 0x8
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
+  - /System/Library/Frameworks/Security.framework/Versions/A/Security
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 3EED330F-9F5C-3E76-9CF9-45D41C22F169
-  Functions: 700
-  Symbols:   2633
-  CStrings:  1935
+  UUID: 3E09DCF2-EFF8-3CBF-B11F-8FA91BE4A8E6
+  Functions: 746
+  Symbols:   2736
+  CStrings:  1972
 
Symbols:
+ +[ACCConnectionInfo sharedInstance].cold.1
+ +[ACCUserDefaults sharedDefaultsIapd].cold.1
+ +[ACCUserDefaults sharedDefaultsLogging].cold.1
+ +[ACCUserDefaults sharedDefaults].cold.1
+ -[ACCExternalAccessoryProvider hasEAEntitlement]
+ -[ACCExternalAccessoryProvider hasEAEntitlement].cold.1
+ -[ACCExternalAccessoryProvider hasEAEntitlement].cold.2
+ -[ACCExternalAccessoryProvider hasEAEntitlement].cold.3
+ -[ACCExternalAccessoryProvider hasEAProtocols]
+ -[ACCExternalAccessoryProvider hasEAProtocols].cold.1
+ -[ACCExternalAccessoryProvider hasEASandbox]
+ -[ACCExternalAccessoryProvider hasEASandbox].cold.1
+ -[ACCHWComponentAuth authenticateBatteryWithChallenge:completionHandler:]
+ -[ACCHWComponentAuth authenticateBatteryWithChallenge:completionHandler:].cold.1
+ -[ACCHWComponentAuth authenticateTouchControllerWithChallenge:completionHandler:]
+ -[ACCHWComponentAuth authenticateTouchControllerWithChallenge:completionHandler:updateRegistry:]
+ -[ACCHWComponentAuth authenticateTouchControllerWithChallenge:completionHandler:updateRegistry:].cold.1
+ -[ACCHWComponentAuth authenticateVeridianWithChallenge:completionHandler:]
+ -[ACCHWComponentAuth authenticateVeridianWithChallenge:completionHandler:].cold.1
+ -[ACCHWComponentAuth authenticateVeridianWithChallenge:completionHandler:updateRegistry:updateUIProperty:logToAnalytics:]
+ -[ACCHWComponentAuth authenticateVeridianWithChallenge:completionHandler:updateRegistry:updateUIProperty:logToAnalytics:].cold.1
+ -[ACCHWComponentAuth signVeridianChallenge:completionHandler:]
+ -[ACCHWComponentAuth signVeridianChallenge:completionHandler:].cold.1
+ -[ACCHWComponentAuth verifyBatteryMatch:completionHandler:]
+ -[ACCHWComponentAuth verifyBatteryMatch:completionHandler:].cold.1
+ _CFRelease
+ _MergedGlobals.2
+ _SANDBOX_CHECK_NO_REPORT
+ _SecTaskCopyValueForEntitlement
+ _SecTaskCreateFromSelf
+ __121-[ACCHWComponentAuth authenticateVeridianWithChallenge:completionHandler:updateRegistry:updateUIProperty:logToAnalytics:]_block_invoke.33
+ __121-[ACCHWComponentAuth authenticateVeridianWithChallenge:completionHandler:updateRegistry:updateUIProperty:logToAnalytics:]_block_invoke.33.cold.1
+ __121-[ACCHWComponentAuth authenticateVeridianWithChallenge:completionHandler:updateRegistry:updateUIProperty:logToAnalytics:]_block_invoke.33.cold.2
+ __121-[ACCHWComponentAuth authenticateVeridianWithChallenge:completionHandler:updateRegistry:updateUIProperty:logToAnalytics:]_block_invoke.33.cold.3
+ __121-[ACCHWComponentAuth authenticateVeridianWithChallenge:completionHandler:updateRegistry:updateUIProperty:logToAnalytics:]_block_invoke_2.cold.1
+ __121-[ACCHWComponentAuth authenticateVeridianWithChallenge:completionHandler:updateRegistry:updateUIProperty:logToAnalytics:]_block_invoke_2.cold.2
+ __59-[ACCHWComponentAuth verifyBatteryMatch:completionHandler:]_block_invoke.40
+ __59-[ACCHWComponentAuth verifyBatteryMatch:completionHandler:]_block_invoke.40.cold.1
+ __59-[ACCHWComponentAuth verifyBatteryMatch:completionHandler:]_block_invoke.40.cold.2
+ __59-[ACCHWComponentAuth verifyBatteryMatch:completionHandler:]_block_invoke.40.cold.3
+ __59-[ACCHWComponentAuth verifyBatteryMatch:completionHandler:]_block_invoke_2.cold.1
+ __59-[ACCHWComponentAuth verifyBatteryMatch:completionHandler:]_block_invoke_2.cold.2
+ __62-[ACCHWComponentAuth signVeridianChallenge:completionHandler:]_block_invoke.36
+ __62-[ACCHWComponentAuth signVeridianChallenge:completionHandler:]_block_invoke.36.cold.1
+ __62-[ACCHWComponentAuth signVeridianChallenge:completionHandler:]_block_invoke.36.cold.2
+ __62-[ACCHWComponentAuth signVeridianChallenge:completionHandler:]_block_invoke.36.cold.3
+ __62-[ACCHWComponentAuth signVeridianChallenge:completionHandler:]_block_invoke_2.cold.1
+ __62-[ACCHWComponentAuth signVeridianChallenge:completionHandler:]_block_invoke_2.cold.2
+ __73-[ACCHWComponentAuth authenticateBatteryWithChallenge:completionHandler:]_block_invoke.24
+ __73-[ACCHWComponentAuth authenticateBatteryWithChallenge:completionHandler:]_block_invoke.24.cold.1
+ __73-[ACCHWComponentAuth authenticateBatteryWithChallenge:completionHandler:]_block_invoke.24.cold.2
+ __73-[ACCHWComponentAuth authenticateBatteryWithChallenge:completionHandler:]_block_invoke.24.cold.3
+ __73-[ACCHWComponentAuth authenticateBatteryWithChallenge:completionHandler:]_block_invoke_2.cold.1
+ __73-[ACCHWComponentAuth authenticateBatteryWithChallenge:completionHandler:]_block_invoke_2.cold.2
+ __74-[ACCHWComponentAuth authenticateVeridianWithChallenge:completionHandler:]_block_invoke.32
+ __74-[ACCHWComponentAuth authenticateVeridianWithChallenge:completionHandler:]_block_invoke.32.cold.1
+ __74-[ACCHWComponentAuth authenticateVeridianWithChallenge:completionHandler:]_block_invoke.32.cold.2
+ __74-[ACCHWComponentAuth authenticateVeridianWithChallenge:completionHandler:]_block_invoke.32.cold.3
+ __74-[ACCHWComponentAuth authenticateVeridianWithChallenge:completionHandler:]_block_invoke_2.cold.1
+ __74-[ACCHWComponentAuth authenticateVeridianWithChallenge:completionHandler:]_block_invoke_2.cold.2
+ __96-[ACCHWComponentAuth authenticateTouchControllerWithChallenge:completionHandler:updateRegistry:]_block_invoke.29
+ __96-[ACCHWComponentAuth authenticateTouchControllerWithChallenge:completionHandler:updateRegistry:]_block_invoke.29.cold.1
+ __96-[ACCHWComponentAuth authenticateTouchControllerWithChallenge:completionHandler:updateRegistry:]_block_invoke.29.cold.2
+ __96-[ACCHWComponentAuth authenticateTouchControllerWithChallenge:completionHandler:updateRegistry:]_block_invoke.29.cold.3
+ __96-[ACCHWComponentAuth authenticateTouchControllerWithChallenge:completionHandler:updateRegistry:]_block_invoke_2.cold.1
+ __96-[ACCHWComponentAuth authenticateTouchControllerWithChallenge:completionHandler:updateRegistry:]_block_invoke_2.cold.2
+ __MergedGlobals
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_ACCHWComponentAuthServiceProtocol
+ __OBJC_$_PROTOCOL_METHOD_TYPES_ACCHWComponentAuthServiceProtocol
+ ___121-[ACCHWComponentAuth authenticateVeridianWithChallenge:completionHandler:updateRegistry:updateUIProperty:logToAnalytics:]_block_invoke
+ ___121-[ACCHWComponentAuth authenticateVeridianWithChallenge:completionHandler:updateRegistry:updateUIProperty:logToAnalytics:]_block_invoke_2
+ ___59-[ACCHWComponentAuth verifyBatteryMatch:completionHandler:]_block_invoke
+ ___59-[ACCHWComponentAuth verifyBatteryMatch:completionHandler:]_block_invoke_2
+ ___62-[ACCHWComponentAuth signVeridianChallenge:completionHandler:]_block_invoke
+ ___62-[ACCHWComponentAuth signVeridianChallenge:completionHandler:]_block_invoke_2
+ ___73-[ACCHWComponentAuth authenticateBatteryWithChallenge:completionHandler:]_block_invoke
+ ___73-[ACCHWComponentAuth authenticateBatteryWithChallenge:completionHandler:]_block_invoke_2
+ ___74-[ACCHWComponentAuth authenticateVeridianWithChallenge:completionHandler:]_block_invoke
+ ___74-[ACCHWComponentAuth authenticateVeridianWithChallenge:completionHandler:]_block_invoke_2
+ ___96-[ACCHWComponentAuth authenticateTouchControllerWithChallenge:completionHandler:updateRegistry:]_block_invoke
+ ___96-[ACCHWComponentAuth authenticateTouchControllerWithChallenge:completionHandler:updateRegistry:]_block_invoke_2
+ ___block_descriptor_40_e8_32bs_e30_v28?0"NSData"8"NSData"16i24l
+ ___block_descriptor_40_e8_32bs_e36_v36?0B8"NSData"12"NSData"20B28i32l
+ ___block_descriptor_40_e8_32bs_e8_v12?0i8l
+ ___block_descriptor_56_e8_32s40s48bs_e5_v8?0l
+ ___block_descriptor_57_e8_32s40s48bs_e5_v8?0l
+ ___block_descriptor_59_e8_32s40s48bs_e5_v8?0l
+ ___copy_helper_block_e8_32s40s48b
+ _dispatch_get_global_queue
+ _dispatch_sync
+ _getpid
+ _kCFAllocatorDefault
+ _objc_msgSend$authenticateBatteryWithChallenge:completionHandler:
+ _objc_msgSend$authenticateTouchControllerWithChallenge:completionHandler:updateRegistry:
+ _objc_msgSend$authenticateVeridianWithChallenge:completionHandler:
+ _objc_msgSend$authenticateVeridianWithChallenge:completionHandler:updateRegistry:updateUIProperty:logToAnalytics:
+ _objc_msgSend$hasEAEntitlement
+ _objc_msgSend$hasEAProtocols
+ _objc_msgSend$hasEASandbox
+ _objc_msgSend$signVeridianChallenge:completionHandler:
+ _objc_msgSend$verifyBatteryMatch:completionHandler:
+ _sandbox_check
+ acc_policies_shouldHideAccessoryWithModelNumber.cold.1
+ acc_policies_shouldOverrideNameOnAccessoryWithModelNumber.cold.1
+ systemInfo_isDeveloperBuild.cold.1
+ systemInfo_isInternalBuild.cold.1
- _SetupAvailabilityChangedHandlerForServiceEntry.cold.1
- _SetupAvailabilityChangedHandlerForServiceEntry.cold.2
- _SetupAvailabilityChangedHandlerForServiceEntry.cold.3
- __gNotificationName
- __gServerAvailabilityChangedHandler
- __gServerAvailable
- __gServerAvailableToken
- __gServerAvailableTokenLock
- acc_policies_deviceNeedsPreArmDeviceIdentity.alreadyPreArmed
- acc_policies_deviceNeedsPreArmDeviceIdentity.onceToken
- acc_policies_deviceNeedsPreArmDeviceIdentity.preArmDate
- accessoryServer_isServerAvailableForServiceEntry.cold.1
- accessoryServer_registerAvailabilityChangedHandlerForServiceEntry.cold.1
- accessoryServer_registerAvailabilityChangedHandlerForServiceEntry.cold.2
- accessoryServer_registerAvailabilityChangedHandlerForServiceEntry.cold.3
- accessoryServer_unregisterAvailabilityChangedHandlerForServiceEntry.cold.1
CStrings:
+ "Authenticating battery... (completionHandler: %s)"
+ "Authenticating touch controller... (completionHandler: %s)"
+ "Signing battery challenge... (completionHandler: %s)"
+ "Verifying battery match... (completionHandler: %s)"
+ "[#ExternalAccessory] Client not entitled to EA service"
+ "[#ExternalAccessory] Client not sandboxed to EA service"
+ "[#ExternalAccessory] No EA protocols found"
+ "[#ExternalAccessory] Unable to create self task"
+ "authenticateBatteryWithChallenge:completionHandler:"
+ "authenticateTouchControllerWithChallenge:completionHandler:"
+ "authenticateTouchControllerWithChallenge:completionHandler:updateRegistry:"
+ "authenticateVeridianWithChallenge:completionHandler:"
+ "authenticateVeridianWithChallenge:completionHandler:updateRegistry:updateUIProperty:logToAnalytics:"
+ "battery authPassed = %d, fdrValidationStatus %d, authError %d"
+ "battery match verification authError %d"
+ "com.apple.private.externalaccessory.showallaccessories"
+ "com.apple.security.exception.mach-lookup.global-name"
+ "hasEAEntitlement"
+ "hasEAProtocols"
+ "hasEASandbox"
+ "mach-lookup"
+ "no completion handler!"
+ "signVeridianChallenge:completionHandler:"
+ "signed battery challenge authError %d"
+ "touch authPassed = %d, fdrValidationStatus %d, authError %d"
+ "v28@?0@\"NSData\"8@\"NSData\"16i24"
+ "v32@0:8@\"NSData\"16@?<v@?@\"NSData\"@\"NSData\"i>24"
+ "v32@0:8@\"NSData\"16@?<v@?B@\"NSData\"@\"NSData\"Bi>24"
+ "v32@0:8@\"NSData\"16@?<v@?i>24"
+ "v36@0:8@\"NSData\"16@?<v@?B@\"NSData\"@\"NSData\"Bi>24B32"
+ "v36@0:8@16@?24B32"
+ "v36@?0B8@\"NSData\"12@\"NSData\"20B28i32"
+ "v44@0:8@\"NSData\"16@?<v@?B@\"NSData\"@\"NSData\"Bi>24B32B36B40"
+ "v44@0:8@16@?24B32B36B40"
+ "verifyBatteryMatch:completionHandler:"

```
