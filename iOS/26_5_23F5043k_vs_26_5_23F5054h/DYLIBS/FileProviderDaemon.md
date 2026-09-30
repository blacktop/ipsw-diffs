## FileProviderDaemon

> `/System/Library/PrivateFrameworks/FileProviderDaemon.framework/FileProviderDaemon`

```diff

-4018.120.13.0.0
-  __TEXT.__text: 0xadfec8
+4018.120.17.0.0
+  __TEXT.__text: 0xadfba4
   __TEXT.__auth_stubs: 0x5db0
   __TEXT.__objc_methlist: 0x9d04
-  __TEXT.__const: 0x2be00
+  __TEXT.__const: 0x2bf30
   __TEXT.__cstring: 0x41ef5
   __TEXT.__oslogstring: 0x1ee92
   __TEXT.__gcc_except_tab: 0xe778
   __TEXT.__ustring: 0x176e
   __TEXT.__dlopen_cstrs: 0xc3
-  __TEXT.__constg_swiftt: 0x1361c
-  __TEXT.__swift5_typeref: 0x134e0
+  __TEXT.__constg_swiftt: 0x13628
+  __TEXT.__swift5_typeref: 0x13524
   __TEXT.__swift5_builtin: 0x8d4
-  __TEXT.__swift5_reflstr: 0xe97d
-  __TEXT.__swift5_fieldmd: 0xc7cc
+  __TEXT.__swift5_reflstr: 0xeb5d
+  __TEXT.__swift5_fieldmd: 0xc890
   __TEXT.__swift5_mpenum: 0x134
-  __TEXT.__swift5_assocty: 0x2958
+  __TEXT.__swift5_assocty: 0x2988
   __TEXT.__swift5_capture: 0x16f68
-  __TEXT.__swift5_proto: 0x1c78
-  __TEXT.__swift5_types: 0xbe0
+  __TEXT.__swift5_proto: 0x1c88
+  __TEXT.__swift5_types: 0xbe4
   __TEXT.__swift5_types2: 0x4
   __TEXT.__swift5_protos: 0xb4
   __TEXT.__swift_as_entry: 0xb0
   __TEXT.__swift_as_ret: 0xa4
-  __TEXT.__unwind_info: 0x14cb0
+  __TEXT.__unwind_info: 0x14cd0
   __TEXT.__eh_frame: 0x2699c
   __TEXT.__objc_classname: 0x2473
   __TEXT.__objc_methname: 0x22ef5

   __DATA_CONST.__objc_superrefs: 0x290
   __DATA_CONST.__objc_arraydata: 0x128
   __AUTH_CONST.__auth_got: 0x2ee8
-  __AUTH_CONST.__const: 0x427f0
+  __AUTH_CONST.__const: 0x428b0
   __AUTH_CONST.__cfstring: 0x72c0
   __AUTH_CONST.__objc_const: 0x2cab8
   __AUTH_CONST.__objc_arrayobj: 0xd8

   __AUTH.__objc_data: 0x19b0
   __AUTH.__data: 0x26b8
   __DATA.__objc_ivar: 0xb6c
-  __DATA.__data: 0x8a30
-  __DATA.__bss: 0x28ee0
+  __DATA.__data: 0x8a70
+  __DATA.__bss: 0x290e0
   __DATA.__common: 0x19b
-  __DATA_DIRTY.__objc_data: 0x3ab8
+  __DATA_DIRTY.__objc_data: 0x3aa8
   __DATA_DIRTY.__data: 0xf788
   __DATA_DIRTY.__bss: 0xd978
   __DATA_DIRTY.__common: 0xa48

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 0336AFF8-7CBD-3607-8639-3899FFCE71F7
-  Functions: 29391
-  Symbols:   26036
-  CStrings:  14072
+  UUID: 39DC9B78-DD7B-3A91-A42B-CC78FCEEFFFE
+  Functions: 29402
+  Symbols:   26042
+  CStrings:  14073
 
Symbols:
+ _associated conformance 18FileProviderDaemon21SuperPendingSetStatusOSHAASQ
+ _associated conformance 18FileProviderDaemon21SuperPendingSetStatusOs12CaseIterableAA8AllCasessADP_Sl
+ _symbolic Say_____G 18FileProviderDaemon21SuperPendingSetStatusO
+ _symbolic _____ 18FileProviderDaemon21SuperPendingSetStatusO
+ _symbolic _____yAAySay_____GSiGSSG s15LazyMapSequenceV 18FileProviderDaemon21SuperPendingSetStatusO
+ _symbolic _____y_____G s23_ContiguousArrayStorageC 18FileProviderDaemon21SuperPendingSetStatusO
CStrings:
+ " OR fp_id IS NULL"
+ "SELECT COUNT(is_pending)\n  FROM reconciliation_table INDEXED BY reconciliation_is_pending\n WHERE is_pending IN "
+ "SELECT fp_id, scheduling_timestamp, last_change\n  FROM reconciliation_table INDEXED BY reconciliation_is_pending\n WHERE is_pending IN "
+ "WHERE is_pending IN "
- "SELECT COUNT(is_pending)\n  FROM reconciliation_table INDEXED BY reconciliation_is_pending\n WHERE is_pending == 1"
- "SELECT fp_id, scheduling_timestamp, last_change\n  FROM reconciliation_table INDEXED BY reconciliation_is_pending\n WHERE is_pending == 1"
- "WHERE is_pending = 1 OR fp_id IS NULL"

```
