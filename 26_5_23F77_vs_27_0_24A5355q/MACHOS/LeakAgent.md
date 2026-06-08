## LeakAgent

> `/System/Library/PrivateFrameworks/DVTInstrumentsFoundation.framework/LeakAgent`

```diff

-64575.73.1.0.0
-  __TEXT.__text: 0x31e0
-  __TEXT.__auth_stubs: 0x4a0
-  __TEXT.__objc_stubs: 0xbe0
+64578.129.2.0.0
+  __TEXT.__text: 0x3394
+  __TEXT.__auth_stubs: 0x500
+  __TEXT.__objc_stubs: 0xd80
   __TEXT.__objc_methlist: 0x19c
   __TEXT.__const: 0xb8
-  __TEXT.__gcc_except_tab: 0x3e4
-  __TEXT.__objc_methname: 0x9fd
-  __TEXT.__cstring: 0x524
+  __TEXT.__gcc_except_tab: 0x378
+  __TEXT.__objc_methname: 0xaeb
+  __TEXT.__cstring: 0x649
   __TEXT.__oslogstring: 0x353
-  __TEXT.__objc_classname: 0x35
+  __TEXT.__objc_classname: 0x33
   __TEXT.__objc_methtype: 0x1a6
   __TEXT.__unwind_info: 0xe0
-  __DATA_CONST.__auth_got: 0x260
-  __DATA_CONST.__got: 0xe0
-  __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x180
-  __DATA_CONST.__cfstring: 0x460
+  __DATA_CONST.__const: 0x198
+  __DATA_CONST.__cfstring: 0x6a0
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_intobj: 0x18
   __DATA_CONST.__objc_arraydata: 0x60
   __DATA_CONST.__objc_dictobj: 0x28
+  __DATA_CONST.__auth_got: 0x290
+  __DATA_CONST.__got: 0xf0
+  __DATA_CONST.__auth_ptr: 0x8
   __DATA.__objc_const: 0x288
-  __DATA.__objc_selrefs: 0x3b8
+  __DATA.__objc_selrefs: 0x420
   __DATA.__objc_ivar: 0xc
   __DATA.__objc_data: 0x50
   __DATA.__data: 0x120

   - /System/Library/PrivateFrameworks/Symbolication.framework/Symbolication
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 6E6AD457-9A6C-3B19-8F9D-C111D067E33C
+  UUID: 22861FEE-2AF3-38F7-B853-0447AEBEC705
   Functions: 25
-  Symbols:   117
-  CStrings:  271
+  Symbols:   124
+  CStrings:  320
 
Symbols:
+ _OBJC_CLASS_$_VMUAnalyticsEvent
+ _objc_alloc_init
+ _objc_claimAutoreleasedReturnValue
+ _objc_retain
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x2
+ _objc_retain_x24
+ _objc_retain_x3
+ _objc_retain_x8
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x22
- _objc_retain_x25
Functions:
~ sub_100001008 : 100 -> 108
~ sub_10000106c -> sub_100001074 : 112 -> 116
~ sub_1000010dc -> sub_1000010e8 : 1492 -> 1432
~ sub_1000016b0 -> sub_100001680 : 84 -> 68
~ sub_100001704 -> sub_1000016c4 : 288 -> 232
~ sub_1000018d0 -> sub_100001858 : 92 -> 88
~ sub_10000192c -> sub_1000018b0 : 460 -> 500
~ sub_100001af8 -> sub_100001aa4 : 4928 -> 5624
~ sub_100002f40 -> sub_1000031a4 : 100 -> 96
~ sub_100002fa4 -> sub_100003204 : 100 -> 96
~ sub_100003008 -> sub_100003264 : 696 -> 700
~ sub_1000032c0 -> sub_100003520 : 732 -> 724
~ sub_1000035b0 -> sub_100003808 : 2040 -> 1920
~ sub_100003dc0 -> sub_100003fa0 : 524 -> 520
~ sub_100003fcc -> sub_1000041a8 : 184 -> 160
~ sub_100004150 -> sub_100004314 : 152 -> 136
CStrings:
+ "abandonedMarkingEnabled"
+ "acquireLeakedAddresses"
+ "acquireLeakedCount"
+ "acquireMarkedAddresses"
+ "acquireMarkedCount"
+ "addEnabledOption:value:"
+ "checkAbandoned"
+ "compress"
+ "conservative"
+ "exactScanningEnabled"
+ "forkCorpse"
+ "fullContent"
+ "fullStackHistory"
+ "leakedOnly"
+ "logAndGenerateReceiptForErrorWithFormat:analyticsEvent:"
+ "maxInteriorOffset"
+ "noContent"
+ "numberWithBool:"
+ "numberWithInt:"
+ "objectContentLevel"
+ "populateInfoFromGraph:"
+ "populateInfoFromTask:"
+ "processSnapshotGraphOptions"
+ "rawNames"
+ "readonlyContent"
+ "regionDescriptionOptions"
+ "scanningMask"
+ "send"
+ "setExitStatus:"
+ "showRawClassNames"
+ "vmuTask"
- "logAndGenerateReceiptForErrorWithFormat:"

```
