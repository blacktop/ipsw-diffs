## RespiratoryHealthDaemon

> `/System/Library/PrivateFrameworks/RespiratoryHealthDaemon.framework/RespiratoryHealthDaemon`

```diff

-6106.1.2.11.0
-  __TEXT.__text: 0x879c
-  __TEXT.__auth_stubs: 0x4e0
+6200.2.7.2.1
+  __TEXT.__text: 0x8744
+  __TEXT.__auth_stubs: 0x4c0
   __TEXT.__objc_methlist: 0x914
   __TEXT.__const: 0xb8
   __TEXT.__oslogstring: 0xb66
   __TEXT.__cstring: 0x88e
-  __TEXT.__gcc_except_tab: 0x27c
+  __TEXT.__gcc_except_tab: 0x274
   __TEXT.__unwind_info: 0x288
   __TEXT.__objc_classname: 0x292
-  __TEXT.__objc_methname: 0x2da6
-  __TEXT.__objc_methtype: 0x84a
+  __TEXT.__objc_methname: 0x2d7e
+  __TEXT.__objc_methtype: 0x81d
   __TEXT.__objc_stubs: 0x1e40
   __DATA_CONST.__got: 0x2b0
   __DATA_CONST.__const: 0x1c0

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x9d8
   __DATA_CONST.__objc_superrefs: 0x30
-  __AUTH_CONST.__auth_got: 0x280
+  __AUTH_CONST.__auth_got: 0x270
   __AUTH_CONST.__const: 0xa0
   __AUTH_CONST.__cfstring: 0x840
-  __AUTH_CONST.__objc_const: 0x11e8
+  __AUTH_CONST.__objc_const: 0x11a8
   __AUTH_CONST.__objc_intobj: 0x30
   __AUTH.__objc_data: 0x140
-  __DATA.__objc_ivar: 0xc4
+  __DATA.__objc_ivar: 0xbc
   __DATA.__data: 0x4e0
   __DATA_DIRTY.__objc_data: 0x140
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/RespiratoryHealth.framework/RespiratoryHealth
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 3AB011B7-E9A9-36D9-AAD6-8D5B9A1CA8A9
+  UUID: 89FC2E3B-7A07-33D7-8FC0-277AB37872B2
   Functions: 199
-  Symbols:   1006
-  CStrings:  688
+  Symbols:   1002
+  CStrings:  685
 
Symbols:
- _OBJC_IVAR_$_HDRPOxygenSaturationAnalyzer._lock
- _OBJC_IVAR_$_HDRPOxygenSaturationAnalyzer._lock_shouldReRequestAnalysisWork
- _os_unfair_lock_lock
- _os_unfair_lock_unlock
Functions:
~ -[HDRPOxygenSaturationAnalyzer initWithProfile:oxygenSaturationFeatureStatusProvider:oxygenSaturationCompanionAnalysisFeatureStatusProvider:unitTestDelegate:] : 364 -> 356
~ -[HDRPOxygenSaturationAnalyzer samplesAdded:anchor:] : 168 -> 144
~ -[HDRPOxygenSaturationAnalyzer performWorkForOperation:profile:databaseAccessibilityAssertion:completion:] : 892 -> 836
CStrings:
- "_lock"
- "_lock_shouldReRequestAnalysisWork"
- "{os_unfair_lock_s=\"_os_unfair_lock_opaque\"I}"

```
