## WebCore

> `/System/Library/PrivateFrameworks/WebCore.framework/WebCore`

```diff

-625.1.29.10.28
-  __TEXT.__text: 0x375840c
+625.1.29.10.29
+  __TEXT.__text: 0x3766044
   __TEXT.__objc_methlist: 0x5ad4
   __TEXT.__getClass_cstr: 0x1290
   __TEXT.__dlsym_cstr: 0x7628
-  __TEXT.__const: 0x1b4880
+  __TEXT.__const: 0x1b4830
   __TEXT.__swift5_typeref: 0x2bb
-  __TEXT.__cstring: 0x33594d
+  __TEXT.__cstring: 0x335711
   __TEXT.__constg_swiftt: 0x2e8
   __TEXT.__swift5_fieldmd: 0x17c
   __TEXT.__swift5_reflstr: 0x7f
   __TEXT.__swift5_proto: 0x3c
   __TEXT.__swift5_types: 0x44
-  __TEXT.__gcc_except_tab: 0x36e34
+  __TEXT.__gcc_except_tab: 0x36e38
   __TEXT.__swift5_assocty: 0x1a0
   __TEXT.__swift5_builtin: 0x14
   __TEXT.__oslogstring: 0x13e86
   __TEXT.__ustring: 0x262
-  __TEXT.__unwind_info: 0x77118
+  __TEXT.__unwind_info: 0x77128
   __TEXT.__eh_frame: 0x180c
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_StringProcessing.dylib
-  Functions: 125568
-  Symbols:   158883
-  CStrings:  33280
+  Functions: 125582
+  Symbols:   158897
+  CStrings:  33279
 
Symbols:
+ __ZN3WTF9HashTableINS_3RefIN7WebCore8DatabaseENS_12RawPtrTraitsIS3_EENS_21DefaultRefDerefTraitsIS3_EEEES8_NS_17IdentityExtractorENS_11DefaultHashIS8_EENS_10HashTraitsIS8_EESD_NS_10FastMallocEE3addILNS_17ShouldValidateKeyE1EEENS_18HashTableAddResultINS_17HashTableIteratorISF_S8_S8_S9_SB_SD_SD_EEEEOS8_
+ __ZN3WTF9HashTableINS_3RefIN7WebCore8DatabaseENS_12RawPtrTraitsIS3_EENS_21DefaultRefDerefTraitsIS3_EEEES8_NS_17IdentityExtractorENS_11DefaultHashIS8_EENS_10HashTraitsIS8_EESD_NS_10FastMallocEE6removeEPS8_
+ __ZN7WebCore12DatabaseTask11performTaskEv
+ __ZN7WebCore12wellKnownURLEN3WTF10StringViewES1_
+ __ZN7WebCore14DatabaseThread18recordDatabaseOpenERNS_8DatabaseE
+ __ZN7WebCore14DatabaseThread23unscheduleDatabaseTasksERNS_8DatabaseE
+ __ZN7WebCore14DatabaseThread5startEv
+ __ZN7WebCore14DatabaseThreadC2Ev
+ __ZN7WebCore14SQLTransaction16getNextStatementEv
+ __ZN7WebCore14SQLTransaction19postflightAndCommitEv
+ __ZN7WebCore14SQLTransaction19runCurrentStatementEv
+ __ZN7WebCore21SQLTransactionBackendC1ERNS_14SQLTransactionE
+ __ZN7WebCore24DatabaseTaskSynchronizer13taskCompletedEv
+ __ZN7WebCore25findOriginInWellKnownListERKNS_18SecurityOriginDataENSt3__14spanIKhLm18446744073709551615EEEN3WTF12ASCIILiteralEONS_25WellKnownOriginListPolicyE
+ __ZN7WebCore26isWellKnownRedirectAllowedERKN3WTF3URLE
+ __ZN7WebCore29isWellKnownResponseAcceptableEiN3WTF10StringViewE
+ __ZN7WebCore29parseOriginsFromWellKnownListENSt3__14spanIKhLm18446744073709551615EEEN3WTF12ASCIILiteralEONS_25WellKnownOriginListPolicyE
+ __ZN7WebCore33prefetchedHostnameCountForTestingEv
+ __ZN7WebCoreL20parseCandidatesArrayENSt3__14spanIKhLm18446744073709551615EEEN3WTF12ASCIILiteralEm
- __ZN3WTF23ObjectIdentifierGenericIN7WebCore16WebSocketChannelENS_38ObjectIdentifierThreadSafeAccessTraitsIyEEyE21m_generationProtectedE
- __ZN3WTF3RefIN7WebCore15DatabaseContextENS_12RawPtrTraitsIS2_EENS_21DefaultRefDerefTraitsIS2_EEED2Ev
- __ZN7WebCore18DatagramByteSource4pullERNS_17JSDOMGlobalObjectERNS_28ReadableByteStreamControllerEON3WTF3RefINS_15DeferredPromiseENS5_12RawPtrTraitsIS7_EENS5_21DefaultRefDerefTraitsIS7_EEEE
- __ZN7WebCore18DatagramByteSource6cancelEON3WTF3RefINS_15DeferredPromiseENS1_12RawPtrTraitsIS3_EENS1_21DefaultRefDerefTraitsIS3_EEEE
- __ZN7WebCore22ScriptExecutionContext18setDatabaseContextEPNS_15DatabaseContextE
CStrings:
- "static ObjectIdentifierGeneric<type-parameter-0-0, type-parameter-0-1, type-parameter-0-2> WTF::ObjectIdentifierGeneric<WebCore::WebSocketChannel, WTF::ObjectIdentifierThreadSafeAccessTraits<uint64_t>, unsigned long long>::generate() [T = WebCore::WebSocketChannel, ThreadSafety = WTF::ObjectIdentifierThreadSafeAccessTraits<uint64_t>, RawValue = unsigned long long]"
```
