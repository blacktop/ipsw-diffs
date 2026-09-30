## CloudRecommendationUI

> `/System/Library/PrivateFrameworks/CloudRecommendationUI.framework/CloudRecommendationUI`

```diff

-301.24.1.3.0
-  __TEXT.__text: 0xa3960
+301.24.1.4.0
+  __TEXT.__text: 0xa6400
   __TEXT.__objc_methlist: 0x8b4
-  __TEXT.__const: 0x72e4
+  __TEXT.__const: 0x7334
   __TEXT.__gcc_except_tab: 0x64
-  __TEXT.__cstring: 0x2054
+  __TEXT.__cstring: 0x20b4
   __TEXT.__dlopen_cstrs: 0x15c
-  __TEXT.__constg_swiftt: 0x2830
-  __TEXT.__swift5_typeref: 0x8de4
-  __TEXT.__swift5_reflstr: 0x1c24
-  __TEXT.__swift5_fieldmd: 0x1a14
+  __TEXT.__constg_swiftt: 0x2860
+  __TEXT.__swift5_typeref: 0x8e06
+  __TEXT.__swift5_reflstr: 0x1c54
+  __TEXT.__swift5_fieldmd: 0x1a20
   __TEXT.__swift5_builtin: 0x78
   __TEXT.__swift5_assocty: 0x558
-  __TEXT.__oslogstring: 0x2953
-  __TEXT.__swift5_capture: 0x1330
+  __TEXT.__oslogstring: 0x2a73
+  __TEXT.__swift5_capture: 0x1340
   __TEXT.__swift5_proto: 0x330
   __TEXT.__swift5_types: 0x1ac
   __TEXT.__swift_as_entry: 0x1fc

   __TEXT.__swift_as_ret: 0x20c
   __TEXT.__swift5_protos: 0x8
   __TEXT.__swift5_mpenum: 0x14
-  __TEXT.__unwind_info: 0x2ee8
-  __TEXT.__eh_frame: 0x4a78
+  __TEXT.__unwind_info: 0x2f78
+  __TEXT.__eh_frame: 0x4b98
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x1c0
+  __DATA_CONST.__const: 0x1d0
   __DATA_CONST.__objc_classlist: 0x178
   __DATA_CONST.__objc_protolist: 0xb0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xb78
+  __DATA_CONST.__objc_selrefs: 0xb80
   __DATA_CONST.__objc_protorefs: 0x58
   __DATA_CONST.__objc_superrefs: 0x18
-  __DATA_CONST.__got: 0xb48
+  __DATA_CONST.__got: 0xb50
   __AUTH_CONST.__const: 0x4928
-  __AUTH_CONST.__objc_const: 0x4f88
-  __AUTH_CONST.__auth_got: 0x16d8
+  __AUTH_CONST.__objc_const: 0x4fa8
+  __AUTH_CONST.__auth_got: 0x16f0
   __AUTH.__objc_data: 0x1260
-  __AUTH.__data: 0x2f28
+  __AUTH.__data: 0x2f68
   __DATA.__objc_ivar: 0x20
-  __DATA.__data: 0x24d0
+  __DATA.__data: 0x24f0
   __DATA.__common: 0x150
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/Combine.framework/Combine

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 3090
-  Symbols:   1930
-  CStrings:  414
+  Functions: 3112
+  Symbols:   1936
+  CStrings:  419
 
Symbols:
+ _CFPreferencesCopyValue
+ _CFPreferencesSetValue
+ _CFPreferencesSynchronize
+ ___swift_closure_destructor.301Tm
+ ___swift_closure_destructor.325Tm
+ _kCFPreferencesAnyUser
+ _kCFPreferencesCurrentHost
+ _objc_msgSend$boolValue
+ _objc_msgSend$initWithBool:
+ _objc_msgSend$setSectionFooter:
+ _objc_msgSend$setSectionHeader:
+ _objc_msgSend$setSectionID:
+ _symbolic _____yShySSGG 2os21OSAllocatedUnfairLockV
+ _symbolic _____yShySSG_____G s13ManagedBufferCsRi__rlE So16os_unfair_lock_sV
- _OBJC_CLASS_$_NSUserDefaults
- ___swift_closure_destructor.298Tm
- ___swift_closure_destructor.322Tm
- ___swift_closure_destructor.428Tm
- _objc_msgSend$boolForKey:
- _objc_msgSend$initWithSuiteName:
- _objc_msgSend$setValue:forKey:
- _objc_msgSend$standardUserDefaults
CStrings:
+ "%s Client filter bypass is set. Force rendering %ld dropped client donated recommendations: %s"
+ "%s No server rule for forced client card %s. Completing it on device with the donor supplied copy."
+ "CLIENT_DONATED_DEBUG"
+ "Client Donated (Internal)"
+ "Could not fetch client donated recommendations from the plugin loader %@"
+ "assembleRecommendationSection(shouldSendDisplayedStatus:shouldRefreshBreakout:droppedClientRecommendations:)"
- "assembleRecommendationSection(shouldSendDisplayedStatus:shouldRefreshBreakout:)"
```
