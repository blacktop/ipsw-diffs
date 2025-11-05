## ExtensionFoundation

> `/System/Library/Frameworks/ExtensionFoundation.framework/Versions/A/ExtensionFoundation`

```diff

-202.4.0.0.0
-  __TEXT.__text: 0x9935c
-  __TEXT.__auth_stubs: 0x1ef0
-  __TEXT.__objc_methlist: 0x40a0
+212.4.0.0.0
+  __TEXT.__text: 0x98bbc
+  __TEXT.__auth_stubs: 0x1ea0
+  __TEXT.__objc_methlist: 0x4810
   __TEXT.__const: 0x18e4
-  __TEXT.__gcc_except_tab: 0x844
-  __TEXT.__cstring: 0x76cc
-  __TEXT.__oslogstring: 0x6614
+  __TEXT.__gcc_except_tab: 0x840
+  __TEXT.__cstring: 0x736c
+  __TEXT.__oslogstring: 0x6604
   __TEXT.__dlopen_cstrs: 0xa5
   __TEXT.__constg_swiftt: 0x1820
-  __TEXT.__swift5_typeref: 0x1146
+  __TEXT.__swift5_typeref: 0x116c
   __TEXT.__swift5_reflstr: 0xc42
   __TEXT.__swift5_fieldmd: 0xca0
   __TEXT.__swift5_builtin: 0x3c

   __TEXT.__swift5_types: 0xec
   __TEXT.__swift5_capture: 0x5e8
   __TEXT.__swift5_protos: 0x30
-  __TEXT.__unwind_info: 0x22a0
-  __TEXT.__eh_frame: 0x1230
+  __TEXT.__swift_as_entry: 0x20
+  __TEXT.__swift_as_ret: 0x20
+  __TEXT.__unwind_info: 0x2300
+  __TEXT.__eh_frame: 0x1210
   __TEXT.__objc_classname: 0x889
   __TEXT.__objc_methname: 0x9a8a
   __TEXT.__objc_methtype: 0x11fa
   __TEXT.__objc_stubs: 0x5ae0
-  __DATA_CONST.__got: 0x728
-  __DATA_CONST.__const: 0x448
+  __DATA_CONST.__got: 0x718
+  __DATA_CONST.__const: 0x438
   __DATA_CONST.__objc_classlist: 0x288
   __DATA_CONST.__objc_catlist: 0x40
   __DATA_CONST.__objc_protolist: 0x1b0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2400
+  __DATA_CONST.__objc_selrefs: 0x2480
   __DATA_CONST.__objc_protorefs: 0x100
   __DATA_CONST.__objc_superrefs: 0x150
   __DATA_CONST.__objc_arraydata: 0x370
-  __AUTH_CONST.__auth_got: 0xf88
-  __AUTH_CONST.__const: 0x3378
-  __AUTH_CONST.__cfstring: 0x2cc0
-  __AUTH_CONST.__objc_const: 0x11180
+  __AUTH_CONST.__auth_got: 0xf60
+  __AUTH_CONST.__const: 0x33c8
+  __AUTH_CONST.__cfstring: 0x2ce0
+  __AUTH_CONST.__objc_const: 0x10610
   __AUTH_CONST.__objc_dictobj: 0x320
   __AUTH_CONST.__objc_intobj: 0xa8
   __AUTH_CONST.__objc_arrayobj: 0xa8
-  __AUTH.__objc_data: 0x2fa0
-  __AUTH.__data: 0xb88
+  __AUTH.__objc_data: 0x2e50
+  __AUTH.__data: 0xba0
   __DATA.__objc_ivar: 0x320
-  __DATA.__data: 0x1b10
+  __DATA.__data: 0x1b18
   __DATA.__crash_info: 0x40
   __DATA.__bss: 0x1bb0
   __DATA.__common: 0x410

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  UUID: C92A99B4-4ADF-3935-8B99-B0440F294894
-  Functions: 3457
-  Symbols:   5124
-  CStrings:  3558
+  UUID: 5B609C82-5115-3EE8-BEC6-65771B0CF6F4
+  Functions: 3524
+  Symbols:   5177
+  CStrings:  3542
 
Symbols:
+ +[EXAuditToken auditTokenForCurrentProcess].cold.1
+ +[EXConcreteExtension globalStateQueueForExtension:].cold.1
+ +[EXConcreteExtension globalStateQueueForExtension:].cold.2
+ +[EXConcreteExtensionContextVendor _completionConcurrentQueue].cold.1
+ +[EXConcreteExtensionContextVendor _expirationConcurrentQueue].cold.1
+ +[EXConcreteExtensionContextVendor _extensionContextClass].cold.1
+ +[EXConcreteExtensionContextVendor _extensionDictionary].cold.1
+ +[EXConcreteExtensionContextVendor _extensionPrincipalClass].cold.1
+ +[EXEnumerator config].cold.1
+ +[EXExtensionContextImplementation _derivedExtensionAuxiliaryHostProtocolWithContextClass:].cold.1
+ +[EXFrameworkScanner frameworkPaths].cold.1
+ +[EXFrameworkScanner rootURL].cold.1
+ +[EXPKService defaultService].cold.1
+ +[EXXPCUtil assertIsExtensionProcess].cold.1
+ +[EXXPCUtil sharedInstance].cold.1
+ +[_EXDefaults sharedInstance].cold.1
+ +[_EXPromiseManager sharedInstance].cold.1
+ +[_EXRunningExtension entryPointFunction].cold.1
+ +[_EXRunningExtension sharedInstance].cold.1
+ +[_EXRunningExtensionInfo extensionInfoForCurrentProcess].cold.1
+ +[_EXRunningExtensionInfo notifyExtensionMainCalled].cold.1
+ +[_EXSandboxExtension sandboxed].cold.1
+ +[_EXSceneSessionManager sharedInstance].cold.1
+ +[_EXUtil auditTokenForCurrentProcess].cold.1
+ -[EXConcreteExtension _safelyBeginUsingSynchronously:request:readyHandler:].cold.5
+ -[EXExtensionPointEnumerator nextObject].cold.2
+ -[_EXDefaults allowedUnsandboxedExtensionPoints].cold.1
+ -[_EXDefaults alwaysEnabledExtensionBundleIdentifiers].cold.1
+ -[_EXDefaults appleInternal].cold.1
+ -[_EXDefaults errorTypes].cold.1
+ -[_EXDefaults imageTypes].cold.1
+ -[_EXDefaults plistTypes].cold.1
+ -[_EXDefaults preferInProcessDiscovery].cold.1
+ -[_EXDefaults useItemProviderXPCConnection].cold.1
+ GCC_except_table233
+ GCC_except_table235
+ GCC_except_table237
+ GCC_except_table47
+ _EXAuditTokenForCurrentProcess.cold.1
+ _EXDefaultLog.cold.1
+ _EXDiscoveryLog.cold.1
+ _EXExtensionPredicateForActivationRule.cold.3
+ _EXExtensionPredicateForActivationRule.cold.4
+ _EXLegacyLog.cold.1
+ _EXRegistrationLog.cold.1
+ _EXSignpostLog.cold.1
+ __75-[EXConcreteExtension _safelyBeginUsingSynchronously:request:readyHandler:]_block_invoke.183
+ __75-[EXConcreteExtension _safelyBeginUsingSynchronously:request:readyHandler:]_block_invoke.183.cold.1
+ __75-[EXConcreteExtension _safelyBeginUsingSynchronously:request:readyHandler:]_block_invoke.183.cold.2
+ __75-[EXConcreteExtension _safelyBeginUsingSynchronously:request:readyHandler:]_block_invoke.183.cold.3
+ __75-[EXConcreteExtension _safelyBeginUsingSynchronously:request:readyHandler:]_block_invoke.183.cold.4
+ __86-[EXConcreteExtension _safelyEndUsingRequestWithPKUUID:processAssertion:continuation:]_block_invoke.194
+ __EXConcreteExtensionTearDownRequestWithIdentifier_block_invoke.430
+ __EXConcreteExtensionTearDownRequestWithIdentifier_block_invoke.430.cold.1
+ __EXConcreteExtensionTearDownRequestWithIdentifier_block_invoke.430.cold.2
+ ___EXExtensionGetActivationRules_block_invoke.cold.2
+ ___NSExtensionContextEmitNotifications_block_invoke.cold.1
+ ___swift_async_entry_functlets
+ ___swift_async_ret_functlets
+ __block_literal_global.198
+ __block_literal_global.200
+ __block_literal_global.202
+ __block_literal_global.428
+ __block_literal_global.450
+ __block_literal_global.452
+ __block_literal_global.456
+ _sharedSafePluginQueue.cold.1
+ _symbolic SccySo19_EXExtensionProcessC______pG s5ErrorP
+ block_copy_helper.3
+ block_copy_helper.7
+ block_descriptor.9
+ block_destroy_helper.4
+ block_destroy_helper.8
+ safelyAccessPidForExtensionIdentiferDictionary.cold.1
- GCC_except_table228
- GCC_except_table230
- GCC_except_table232
- GCC_except_table48
- _OUTLINED_FUNCTION_13
- _OUTLINED_FUNCTION_14
- _OUTLINED_FUNCTION_15
- _OUTLINED_FUNCTION_16
- __75-[EXConcreteExtension _safelyBeginUsingSynchronously:request:readyHandler:]_block_invoke.180
- __75-[EXConcreteExtension _safelyBeginUsingSynchronously:request:readyHandler:]_block_invoke.180.cold.1
- __75-[EXConcreteExtension _safelyBeginUsingSynchronously:request:readyHandler:]_block_invoke.180.cold.2
- __75-[EXConcreteExtension _safelyBeginUsingSynchronously:request:readyHandler:]_block_invoke.180.cold.3
- __75-[EXConcreteExtension _safelyBeginUsingSynchronously:request:readyHandler:]_block_invoke.180.cold.4
- __86-[EXConcreteExtension _safelyEndUsingRequestWithPKUUID:processAssertion:continuation:]_block_invoke.191
- __EXConcreteExtensionTearDownRequestWithIdentifier_block_invoke.427
- __EXConcreteExtensionTearDownRequestWithIdentifier_block_invoke.427.cold.1
- __EXConcreteExtensionTearDownRequestWithIdentifier_block_invoke.427.cold.2
- __block_literal_global.193
- __block_literal_global.195
- __block_literal_global.197
- __block_literal_global.199
- __block_literal_global.447
- __block_literal_global.449
- __block_literal_global.453
- block_descriptor.3
CStrings:
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/ExtensionFoundation/ExtensionFoundation/Source/EXExtension/Extension/EXExtensionIdentity.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/ExtensionFoundation/ExtensionFoundation/Source/EXExtension/Extension/Internal/EXConnectionHandlerExtension.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/ExtensionFoundation/ExtensionFoundation/Source/EXExtension/Extension/Internal/EXExtension+Configuration.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/ExtensionFoundation/ExtensionFoundation/Source/EXExtension/Extension/Internal/EXRunningExtension.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/ExtensionFoundation/ExtensionFoundation/Source/EXExtension/Extension/Internal/Shim/EXExtensionContext.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/ExtensionFoundation/ExtensionFoundation/Source/EXExtension/Extension/Internal/Shim/EXNSExtensionContextShimImplementation.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/ExtensionFoundation/ExtensionFoundation/Source/EXExtension/Extension/Internal/Shim/EXNSExtensionShimExtension.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/ExtensionFoundation/ExtensionFoundation/Source/EXExtension/Promise/EXPromise.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/ExtensionFoundation/ExtensionFoundation/Source/EXExtension/Scene/EXSceneSession.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/ExtensionFoundation/ExtensionFoundation/Source/NSExtension/NSExtensionSupport/EXConcreteExtension+Filtering.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/ExtensionFoundation/ExtensionFoundation/Source/NSExtension/NSExtensionSupport/EXConcreteExtension.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/ExtensionFoundation/ExtensionFoundation/Source/NSExtension/NSExtensionSupport/EXConcreteExtensionContextVendor.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/ExtensionFoundation/ExtensionFoundation/Source/NSExtension/NSExtensionSupport/EXExtensionContextImplementation.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/ExtensionFoundation/ExtensionFoundation/Source/NSExtension/NSExtensionSupport/EXPersona.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/ExtensionFoundation/ExtensionFoundation/Source/NSExtension/NSExtensionSupport/ItemProvider/EXLoadOperator.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/ExtensionFoundation/ExtensionFoundation/Source/NSExtension/NSExtensionSupport/NSExtension+ExtensionKitAdditions.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/ExtensionFoundation/ExtensionFoundation/Source/NSExtension/PK Subsystems/EXService_Subsystem.m"
+ "Disallowing host app state observation due to Info.plist override."
+ "_EXIgnoreHostAppStateChanges"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/ExtensionFoundation/ExtensionFoundation/Source/EXExtension/Extension/EXExtensionIdentity.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/ExtensionFoundation/ExtensionFoundation/Source/EXExtension/Extension/Internal/EXConnectionHandlerExtension.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/ExtensionFoundation/ExtensionFoundation/Source/EXExtension/Extension/Internal/EXExtension+Configuration.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/ExtensionFoundation/ExtensionFoundation/Source/EXExtension/Extension/Internal/EXRunningExtension.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/ExtensionFoundation/ExtensionFoundation/Source/EXExtension/Extension/Internal/Shim/EXExtensionContext.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/ExtensionFoundation/ExtensionFoundation/Source/EXExtension/Extension/Internal/Shim/EXNSExtensionContextShimImplementation.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/ExtensionFoundation/ExtensionFoundation/Source/EXExtension/Extension/Internal/Shim/EXNSExtensionShimExtension.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/ExtensionFoundation/ExtensionFoundation/Source/EXExtension/Promise/EXPromise.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/ExtensionFoundation/ExtensionFoundation/Source/EXExtension/Scene/EXSceneSession.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/ExtensionFoundation/ExtensionFoundation/Source/NSExtension/NSExtensionSupport/EXConcreteExtension+Filtering.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/ExtensionFoundation/ExtensionFoundation/Source/NSExtension/NSExtensionSupport/EXConcreteExtension.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/ExtensionFoundation/ExtensionFoundation/Source/NSExtension/NSExtensionSupport/EXConcreteExtensionContextVendor.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/ExtensionFoundation/ExtensionFoundation/Source/NSExtension/NSExtensionSupport/EXExtensionContextImplementation.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/ExtensionFoundation/ExtensionFoundation/Source/NSExtension/NSExtensionSupport/EXPersona.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/ExtensionFoundation/ExtensionFoundation/Source/NSExtension/NSExtensionSupport/ItemProvider/EXLoadOperator.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/ExtensionFoundation/ExtensionFoundation/Source/NSExtension/NSExtensionSupport/NSExtension+ExtensionKitAdditions.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/ExtensionFoundation/ExtensionFoundation/Source/NSExtension/PK Subsystems/EXService_Subsystem.m"
- "Insufficient space allocated to copy string contents"
- "Negative value is not representable"
- "Not enough bits to represent the passed value"
- "Process is nil with no error for launch configuration: %{public}@"
- "Swift/ContiguousArrayBuffer.swift"
- "Swift/Integers.swift"
- "Swift/StringTesting.swift"
- "Swift/StringUTF8View.swift"
- "Swift/UnsafeBufferPointer.swift"
- "Swift/UnsafePointer.swift"
- "Swift/UnsafeRawBufferPointer.swift"
- "Swift/UnsafeRawPointer.swift"
- "Unexpectedly found nil while unwrapping an Optional value"
- "UnsafeMutableBufferPointer with negative count"
- "UnsafeMutablePointer.initialize overlapping range"
- "UnsafeMutablePointer.initialize with negative count"
- "UnsafeMutableRawBufferPointer.copyMemory source has too many elements"
- "UnsafeMutableRawPointer.initializeMemory overlapping range"
- "invalid Collection: less than 'count' elements in collection"

```
