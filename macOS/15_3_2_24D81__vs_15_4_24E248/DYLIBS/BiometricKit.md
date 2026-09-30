## BiometricKit

> `/System/Library/PrivateFrameworks/BiometricKit.framework/Versions/A/BiometricKit`

```diff

-506.60.1.0.0
-  __TEXT.__text: 0x30254
-  __TEXT.__auth_stubs: 0x510
-  __TEXT.__objc_methlist: 0x2490
+511.100.15.0.0
+  __TEXT.__text: 0x30c3c
+  __TEXT.__auth_stubs: 0x550
+  __TEXT.__objc_methlist: 0x29f4
   __TEXT.__const: 0x148
   __TEXT.__oslogstring: 0x39d6
-  __TEXT.__cstring: 0x18af
-  __TEXT.__gcc_except_tab: 0xc98
-  __TEXT.__unwind_info: 0xdf0
+  __TEXT.__cstring: 0x18aa
+  __TEXT.__gcc_except_tab: 0xc9c
+  __TEXT.__unwind_info: 0xe40
   __TEXT.__objc_classname: 0x4e7
-  __TEXT.__objc_methname: 0x5953
+  __TEXT.__objc_methname: 0x59af
   __TEXT.__objc_methtype: 0x1232
   __TEXT.__objc_stubs: 0x3380
   __DATA_CONST.__got: 0x1f0

   __DATA_CONST.__objc_classlist: 0x178
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1570
+  __DATA_CONST.__objc_selrefs: 0x1608
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0xd0
   __DATA_CONST.__objc_arraydata: 0x50
-  __AUTH_CONST.__auth_got: 0x298
+  __AUTH_CONST.__auth_got: 0x2b8
   __AUTH_CONST.__const: 0xd10
   __AUTH_CONST.__cfstring: 0x10e0
-  __AUTH_CONST.__objc_const: 0x5c70
+  __AUTH_CONST.__objc_const: 0x5270
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__objc_intobj: 0x60
   __AUTH.__objc_data: 0x230
-  __DATA.__objc_ivar: 0x2e0
+  __DATA.__objc_ivar: 0x2e4
   __DATA.__data: 0x2a0
   __DATA.__bss: 0x81
   __DATA_DIRTY.__objc_data: 0xc80

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 4177A90D-4542-3EA1-8FAB-E440078822E0
-  Functions: 1115
-  Symbols:   2474
-  CStrings:  1893
+  UUID: 8D1ED762-293C-3EFB-9A5A-AECAFE157BF6
+  Functions: 1210
+  Symbols:   2591
+  CStrings:  1897
 
Symbols:
+ +[BKDeviceDescriptor initialize].cold.1
+ +[BKDeviceManager initialize].cold.1
+ +[BKDeviceTouchID deviceAvailableWithFailure:].cold.1
+ +[BiometricSupportTools analyticsOSLogNSDictionary:forEvent:toLogPath:withPrefix:].cold.1
+ +[BiometricSupportTools analyticsOSLogNSDictionary:forEvent:toLogPath:withPrefix:].cold.2
+ -[BKDevice createEnrollOperationWithError:].cold.1
+ -[BKDevice createMatchOperationWithError:].cold.1
+ -[BKDevice createPresenceDetectOperationWithError:].cold.1
+ -[BKDevice dropAllUnlockTokensWithError:].cold.1
+ -[BKDevice forceBioLockoutForAllUsersWithError:].cold.1
+ -[BKDevice identitiesDatabaseHashForUser:error:].cold.1
+ -[BKDevice identitiesDatabaseUUIDForUser:error:].cold.1
+ -[BKDevice setProtectedConfiguration:forUser:credentialSet:async:reply:].cold.1
+ -[BKDevice setSystemProtectedConfiguration:credentialSet:async:reply:].cold.1
+ -[BKDevice setSystemProtectedConfiguration:credentialSet:async:reply:].cold.2
+ -[BKDevice setSystemProtectedConfiguration:credentialSet:async:reply:].cold.3
+ -[BKDevice setSystemProtectedConfiguration:credentialSet:async:reply:].cold.4
+ -[BKDeviceTouchID createEnrollOperationWithError:].cold.1
+ -[BKDeviceTouchID createExtendEnrollTouchIDOperationWithError:].cold.1
+ -[BKDeviceTouchID createMatchOperationWithError:].cold.1
+ -[BKDeviceTouchID createPresenceDetectOperationWithError:].cold.1
+ -[BKDeviceTouchID enableBackgroundFingerDetection:error:].cold.1
+ -[BKMatchPearlOperation nonDelayedIndicator]
+ -[BKMatchPearlOperation setNonDelayedIndicator:]
+ -[BiometricKitXPCClientConnection initWithDeviceType:].cold.1
+ ComponentSetUpdate.cold.1
+ ComponentSetUpdate.cold.10
+ ComponentSetUpdate.cold.11
+ ComponentSetUpdate.cold.12
+ ComponentSetUpdate.cold.13
+ ComponentSetUpdate.cold.14
+ ComponentSetUpdate.cold.15
+ ComponentSetUpdate.cold.16
+ ComponentSetUpdate.cold.17
+ ComponentSetUpdate.cold.18
+ ComponentSetUpdate.cold.19
+ ComponentSetUpdate.cold.2
+ ComponentSetUpdate.cold.20
+ ComponentSetUpdate.cold.21
+ ComponentSetUpdate.cold.22
+ ComponentSetUpdate.cold.23
+ ComponentSetUpdate.cold.24
+ ComponentSetUpdate.cold.25
+ ComponentSetUpdate.cold.3
+ ComponentSetUpdate.cold.4
+ ComponentSetUpdate.cold.5
+ ComponentSetUpdate.cold.6
+ ComponentSetUpdate.cold.7
+ ComponentSetUpdate.cold.8
+ ComponentSetUpdate.cold.9
+ GenerateMatchTemplateTopology.cold.1
+ GenerateMatchTemplateTopology.cold.2
+ GenerateMatchTemplateTopology.cold.3
+ GenerateMatchTemplateTopology.cold.4
+ GenerateMatchTemplateTopology.cold.5
+ GenerateTemplateTopology.cold.1
+ GenerateTemplateTopology.cold.2
+ GenerateTemplateTopology.cold.3
+ GenerateTemplateTopology.cold.4
+ GenerateTemplateTopologyInfo.cold.1
+ OBJC_IVAR_$_BKMatchPearlOperation._nonDelayedIndicator
+ _BKLogEventOrCode.cold.1
+ _CFPreferencesCopyAppValue
+ _OUTLINED_FUNCTION_0
+ _OUTLINED_FUNCTION_1
+ _OUTLINED_FUNCTION_10
+ _OUTLINED_FUNCTION_11
+ _OUTLINED_FUNCTION_12
+ _OUTLINED_FUNCTION_13
+ _OUTLINED_FUNCTION_14
+ _OUTLINED_FUNCTION_15
+ _OUTLINED_FUNCTION_16
+ _OUTLINED_FUNCTION_17
+ _OUTLINED_FUNCTION_2
+ _OUTLINED_FUNCTION_3
+ _OUTLINED_FUNCTION_4
+ _OUTLINED_FUNCTION_5
+ _OUTLINED_FUNCTION_6
+ _OUTLINED_FUNCTION_7
+ _OUTLINED_FUNCTION_8
+ _OUTLINED_FUNCTION_9
+ __FindLargestComponent.cold.1
+ __FindLargestComponent.cold.2
+ __GenerateTemplateTopology.cold.1
+ __GenerateTemplateTopology.cold.2
+ __RebaseComponent.cold.1
+ __RebaseComponent.cold.2
+ __RebaseComponent.cold.3
+ __RebaseComponent.cold.4
+ __RebaseComponent.cold.5
+ __RebaseComponent.cold.6
+ __RebaseComponent.cold.7
+ __TranslateNodePlacement.cold.1
+ __TranslateNodePlacement.cold.2
+ __TranslateNodePlacement.cold.3
+ __TranslateNodePlacement.cold.4
+ _dispatch_queue_attr_make_with_autorelease_frequency
+ _objc_autoreleasePoolPop
+ _objc_autoreleasePoolPush
+ isEphemeralMultiUser.cold.1
+ isFaceIDPlatform.cold.1
+ isInternalBuild.cold.1
- -[BiometricKit init].cold.1
- -[BiometricKit init].cold.2
CStrings:
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/BiometricKit/TouchID/nodevis.c"
+ "TB,N,V_nonDelayedIndicator"
+ "_nonDelayedIndicator"
+ "com.apple.MCX._managementStatusChangedForDomains"
+ "histogram != ((void*)0)"
+ "newVertex != ((void*)0)"
+ "nonDelayedIndicator"
+ "set->components[newVertex->componentIndex] != ((void*)0)"
+ "setNonDelayedIndicator:"
+ "tmp != ((void*)0)"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/BiometricKit/TouchID/nodevis.c"
- "com.apple.ManagedConfiguration.profileListChanged"
- "histogram != ((void *)0)"
- "newVertex != ((void *)0)"
- "set->components[newVertex->componentIndex] != ((void *)0)"
- "tmp != ((void *)0)"

```
