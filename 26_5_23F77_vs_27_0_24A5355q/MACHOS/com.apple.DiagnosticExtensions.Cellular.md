## com.apple.DiagnosticExtensions.Cellular

> `/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/com.apple.DiagnosticExtensions.Cellular.appex/com.apple.DiagnosticExtensions.Cellular`

```diff

-1418.1.0.0.0
-  __TEXT.__text: 0x25a5c
-  __TEXT.__auth_stubs: 0xbc0
+1563.0.0.0.0
+  __TEXT.__text: 0x259d4
+  __TEXT.__auth_stubs: 0xbb0
   __TEXT.__objc_stubs: 0x5c0
-  __TEXT.__init_offsets: 0x8
+  __TEXT.__init_offsets: 0x10
   __TEXT.__objc_methlist: 0x1a8
   __TEXT.__const: 0x4a0
-  __TEXT.__gcc_except_tab: 0x35ec
-  __TEXT.__cstring: 0x4a0
-  __TEXT.__oslogstring: 0xb38
+  __TEXT.__gcc_except_tab: 0x33c4
+  __TEXT.__cstring: 0x4cd
+  __TEXT.__oslogstring: 0xb1e
   __TEXT.__objc_methname: 0x47e
-  __TEXT.__objc_classname: 0x46
+  __TEXT.__objc_classname: 0x44
   __TEXT.__objc_methtype: 0x288
-  __TEXT.__unwind_info: 0x778
-  __DATA_CONST.__auth_got: 0x5f0
-  __DATA_CONST.__got: 0x2f8
+  __TEXT.__unwind_info: 0x7a8
   __DATA_CONST.__const: 0x9a0
   __DATA_CONST.__cfstring: 0x2a0
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x10
   __DATA_CONST.__objc_intobj: 0x30
+  __DATA_CONST.__auth_got: 0x5e8
+  __DATA_CONST.__got: 0x308
   __DATA.__objc_const: 0x300
   __DATA.__objc_selrefs: 0x1a8
   __DATA.__objc_ivar: 0x28
   __DATA.__objc_data: 0xf0
-  __DATA.__data: 0xa0
-  __DATA.__bss: 0x80
+  __DATA.__data: 0xf0
+  __DATA.__bss: 0xc8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/ABMHelper.framework/ABMHelper

   - /usr/lib/libTelephonyUtilDynamic.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 50593546-0B30-3F03-8006-B54DD7B52C87
-  Functions: 289
-  Symbols:   377
-  CStrings:  268
+  UUID: E42F0494-DC20-3358-9929-60C72E3F0033
+  Functions: 295
+  Symbols:   385
+  CStrings:  270
 
Symbols:
+ _CFPreferencesSetValue
+ _CFPreferencesSynchronize
+ _TelephonyBasebandWatchdogStartWithStackshot
+ _TelephonyBasebandWatchdogStop
+ __ZN3abm14kTraceSettingsE
+ __ZN3abm21getChannelPropertyKeyEmRKNSt3__112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE
+ __ZN3abm25kKeyTraceSettingsSelectedE
+ __ZN3abm29kKeyTraceChannelHistorySizeMBE
+ __ZN3abm33kKeyTracePropertyTriggerInterfaceE
+ __ZN3abm8asStringENS_16TriggerInterfaceE
+ __ZN3ctu2cf12convert_copyERPK10__CFStringRKNSt3__112basic_stringIcNS5_11char_traitsIcEENS5_9allocatorIcEEEEjPK13__CFAllocator
+ __ZN3ctu2cf13plist_adapterC1EPK10__CFStringS4_
+ __ZN3ctu2cf13plist_adapterD1Ev
+ __ZN3ctu2cf6assignERNSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEEPKv
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE21__grow_by_and_replaceEmmmmmmPKc
+ _kCFPreferencesCurrentHost
+ _kCFPreferencesCurrentUser
+ _objc_claimAutoreleasedReturnValue
+ _objc_retain_x22
- __ZN12capabilities5trace7allowedEv
- __ZN12capabilities5trace8asStringENS0_14SleepTraceModeE
- __ZN3abm14kTraceCoreDumpE
- __ZN3abm21kKeyTracePrivacyLevelE
- __ZN8defaults7bbtrace12privacyLevelEv
- __ZN8defaults7bbtrace16trace_sleep_modeEv
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6appendEPKcm
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6insertEmPKcm
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x23
- _objc_retain_x24
CStrings:
+ "Carrier"
+ "Customer"
+ "Watchdog timed out"
+ "boot-args='([^']*)'"
- "Invalid privacy level: %d"
- "PrivacyLevel"

```
