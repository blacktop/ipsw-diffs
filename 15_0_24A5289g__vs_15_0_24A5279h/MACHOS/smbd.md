## smbd

> `/usr/sbin/smbd`

```diff

-646.0.0.0.0
-  __TEXT.__text: 0x84940
-  __TEXT.__auth_stubs: 0x2010
+644.0.0.0.0
+  __TEXT.__text: 0x85080
+  __TEXT.__auth_stubs: 0x2000
   __TEXT.__init_offsets: 0x1c
   __TEXT.__const: 0x1287
-  __TEXT.__gcc_except_tab: 0x5e04
+  __TEXT.__gcc_except_tab: 0x5e7c
   __TEXT.__oslogstring: 0x9d87
-  __TEXT.__cstring: 0x1040e
+  __TEXT.__cstring: 0x10454
   __TEXT.__dof_ntvfs: 0x1eed
   __TEXT.__dof_smbd: 0x7aa
   __TEXT.__unwind_info: 0x21f8
-  __DATA_CONST.__auth_got: 0x1010
+  __DATA_CONST.__auth_got: 0x1008
   __DATA_CONST.__got: 0x1d0
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0xa820
+  __DATA_CONST.__const: 0xa800
   __DATA_CONST.__cfstring: 0x200
   __DATA.__data: 0xa78
   __DATA.__crash_info: 0x40
   __DATA.__common: 0x100
-  __DATA.__bss: 0x298
+  __DATA.__bss: 0x370
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/DiskArbitration.framework/Versions/A/DiskArbitration
   - /System/Library/Frameworks/GSS.framework/Versions/A/GSS

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libpam.2.dylib
-  Functions: 1638
-  Symbols:   3186
-  CStrings:  2468
+  Functions: 1635
+  Symbols:   3190
+  CStrings:  2474
 
Symbols:
+ __ZL14SessionsSigned
+ __ZL15SessionAuthLKDC
+ __ZL16SessionsAuthKRB5
+ __ZL16SessionsAuthNTLM
+ __ZL16SessionsUnsigned
+ __ZL19SessionsDialect0202
+ __ZL19SessionsDialect0210
+ __ZL19SessionsDialect0300
+ __ZL19SessionsDialect0302
+ __ZL19SessionsDialectSMB1
+ __ZL26session_analytics_event_id
+ __ZN15smbd_statistics14smbd_analytics20addAuthMechStatisticERKNSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE
+ __ZN15smbd_statistics14smbd_analytics26addSessionDialectStatisticEt
+ __ZN15smbd_statistics14smbd_analytics26addSessionSigningStatisticEb
+ __block_descriptor_tmp.44
- __ZL21smbd_session_event_id
- __ZL24smbd_statistics_event_id
- __ZN15smbd_statistics14smbd_analytics19sessAuthFromMechStrERKNSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE
- __ZN15smbd_statistics14smbd_analytics20addSessionStatisticsERKNSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEEtb
- __ZN15smbd_statistics14smbd_analytics20sendSessionAnalyticsENS_15SessionAuthEnumENS_18SessionDialectEnumEb
- __ZN15smbd_statistics14smbd_analytics24addSMB1SessionStatisticsERKNSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEEb
- __ZN15smbd_statistics14smbd_analytics26sessDialectEnumFromDialectEt
- ____ZN15smbd_statistics14smbd_analytics20sendSessionAnalyticsENS_15SessionAuthEnumENS_18SessionDialectEnumEb_block_invoke
- __block_descriptor_tmp.29
- __block_descriptor_tmp.30
- _xpc_dictionary_set_bool
CStrings:
+ "/AppleInternal/Library/BuildRoots/7abfe40b-2884-11ef-836f-e2437461156c/Library/Caches/com.apple.xbs/Sources/smbx/ext/gflags-1.1/src/gflags_reporting.cc"
+ "/AppleInternal/Library/BuildRoots/7abfe40b-2884-11ef-836f-e2437461156c/Library/Caches/com.apple.xbs/Sources/smbx/src/cmd/smbd/smbd.cpp"
+ "SESSION_0202"
+ "SESSION_0210"
+ "SESSION_0300"
+ "SESSION_0302"
+ "SESSION_AUTH_KRB5"
+ "SESSION_AUTH_LKDC"
+ "SESSION_AUTH_NTLM"
+ "SESSION_SIGNED"
+ "SESSION_SMB1"
+ "SESSION_UNSIGNED"
+ "addAuthMechStatistic"
+ "addSessionDialectStatistic"
- "/AppleInternal/Library/BuildRoots/c496718d-33c1-11ef-b26f-e2437461156c/Library/Caches/com.apple.xbs/Sources/smbx/ext/gflags-1.1/src/gflags_reporting.cc"
- "/AppleInternal/Library/BuildRoots/c496718d-33c1-11ef-b26f-e2437461156c/Library/Caches/com.apple.xbs/Sources/smbx/src/cmd/smbd/smbd.cpp"
- "SessionAuthentication"
- "SessionDialect"
- "SessionSigned"
- "com.apple.smbd.session.created"
- "sessAuthFromMechStr"
- "sessDialectEnumFromDialect"

```
