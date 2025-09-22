## CalendarDaemon

> `/System/Library/PrivateFrameworks/CalendarDaemon.framework/CalendarDaemon`

```diff

-1224.0.0.0.0
-  __TEXT.__text: 0x71590
-  __TEXT.__auth_stubs: 0x3820
+1224.1.2.0.0
+  __TEXT.__text: 0x7165c
+  __TEXT.__auth_stubs: 0x3840
   __TEXT.__objc_methlist: 0x6184
-  __TEXT.__cstring: 0x6f58
+  __TEXT.__cstring: 0x6f7d
   __TEXT.__const: 0x150
   __TEXT.__oslogstring: 0x81fe
   __TEXT.__gcc_except_tab: 0x1ba4

   __TEXT.__ustring: 0x4
   __TEXT.__unwind_info: 0x1ad8
   __TEXT.__objc_classname: 0x1499
-  __TEXT.__objc_methname: 0xeaaa
+  __TEXT.__objc_methname: 0xead1
   __TEXT.__objc_methtype: 0x6639
   __TEXT.__objc_stubs: 0x9bc0
   __DATA_CONST.__got: 0x9e8

   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x2a8
   __DATA_CONST.__objc_arraydata: 0x350
-  __AUTH_CONST.__auth_got: 0x1c20
+  __AUTH_CONST.__auth_got: 0x1c30
   __AUTH_CONST.__const: 0x880
-  __AUTH_CONST.__cfstring: 0x79a0
-  __AUTH_CONST.__objc_const: 0xc0f0
+  __AUTH_CONST.__cfstring: 0x79e0
+  __AUTH_CONST.__objc_const: 0xc130
   __AUTH_CONST.__objc_intobj: 0x468
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH.__objc_data: 0x1400
   __AUTH.__data: 0xa50
-  __DATA.__objc_ivar: 0x788
+  __DATA.__objc_ivar: 0x790
   __DATA.__data: 0x1728
   __DATA.__bss: 0x198
   __DATA.__common: 0x8

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 93A88941-C2B1-3CC2-BAC6-D20CAF1D40C6
+  UUID: 999EDBAB-3C1E-3167-BCEB-55BBAF49C0F0
   Functions: 2149
-  Symbols:   8945
-  CStrings:  5551
+  Symbols:   8949
+  CStrings:  5557
 
Symbols:
+ _CalCalendarCopyDomainName
+ _CalCalendarEmailIsUsedForOtherSource
+ _OBJC_IVAR_$_CADStatsStoreInfo._emailDomain
+ _OBJC_IVAR_$_CADStatsStoreInfo._emailIsUsedInOtherSource
Functions:
~ -[CADStatsStores processStores:] : 484 -> 564
~ -[CADStatsStores eventDictionaries] : 588 -> 656
~ -[CADStatsStoreInfo .cxx_destruct] : 12 -> 68
CStrings:
+ "_emailDomain"
+ "_emailIsUsedInOtherSource"
+ "emailDomain"
+ "emailIsUsedInOtherSource"

```
