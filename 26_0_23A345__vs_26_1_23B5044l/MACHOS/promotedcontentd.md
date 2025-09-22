## promotedcontentd

> `/usr/libexec/promotedcontentd`

```diff

-556.0.83.0.0
-  __TEXT.__text: 0x38f9c8
+556.1.3.0.0
+  __TEXT.__text: 0x38faa4
   __TEXT.__auth_stubs: 0x4010
   __TEXT.__objc_stubs: 0x18860
   __TEXT.__objc_methlist: 0x15234
   __TEXT.__const: 0x2a120
   __TEXT.__objc_methname: 0x25aca
   __TEXT.__oslogstring: 0xec6b
-  __TEXT.__cstring: 0x13a46
+  __TEXT.__cstring: 0x13bb6
   __TEXT.__objc_classname: 0x2748
   __TEXT.__objc_methtype: 0x4c5a
   __TEXT.__gcc_except_tab: 0x177c
   __TEXT.__constg_swiftt: 0x4474
-  __TEXT.__swift5_typeref: 0x2ea4
+  __TEXT.__swift5_typeref: 0x2e86
   __TEXT.__swift5_reflstr: 0x1eac
   __TEXT.__swift5_fieldmd: 0x3150
   __TEXT.__swift5_builtin: 0x104
   __TEXT.__swift5_assocty: 0x250
   __TEXT.__swift5_proto: 0x694
   __TEXT.__swift5_types: 0x418
-  __TEXT.__swift5_capture: 0x8d4
+  __TEXT.__swift5_capture: 0x8e4
   __TEXT.__swift5_protos: 0xc4
   __TEXT.__swift_as_entry: 0x6c
   __TEXT.__swift_as_ret: 0x88

   __DATA_CONST.__auth_got: 0x2018
   __DATA_CONST.__got: 0x10f8
   __DATA_CONST.__auth_ptr: 0xe68
-  __DATA_CONST.__const: 0x1d008
-  __DATA_CONST.__cfstring: 0xf2c0
+  __DATA_CONST.__const: 0x1d020
+  __DATA_CONST.__cfstring: 0xf2e0
   __DATA_CONST.__objc_classlist: 0xe38
   __DATA_CONST.__objc_catlist: 0xb8
   __DATA_CONST.__objc_protolist: 0x2c0

   __DATA.__objc_selrefs: 0x93a8
   __DATA.__objc_ivar: 0x14ec
   __DATA.__objc_data: 0x8c90
-  __DATA.__data: 0x9b10
+  __DATA.__data: 0x9b00
   __DATA.__common: 0xc48
   __DATA.__bss: 0xbdb8
   - /AppleInternal/Library/Frameworks/TestHookService.framework/TestHookService

   - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
-  - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftMetal.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 05527D28-919E-334A-89F4-1B5DF031A3CC
-  Functions: 10337
-  Symbols:   2235
-  CStrings:  13744
+  UUID: 7BC29A72-32BD-328C-B682-6215A245C446
+  Functions: 10339
+  Symbols:   2234
+  CStrings:  13747
 
Symbols:
- __swift_FORCE_LOAD_$_swiftCoreImage
CStrings:
+ "SELECT t.rowid, t.experimentId, t.treatmentId FROM APDBTrigger AS t INNER JOIN APDBExperimentationReport AS er ON er.triggerRowId = t.rowid WHERE er.day = ? AND er.source = ? AND (er.slotVisibleAdCount + er.slotVisibleNoAdCount + er.impressionCount + er.clickCount + er.downloadCount + er.redownloadCount + er.preOrderPlacedCount + er.viewDownloadCount + er.viewRedownloadCount + er.viewPreorderPlacedCount) > 0 GROUP BY t.rowid LIMIT %ld OFFSET %ld"
+ "[RotatingIdentifierXPCReceiver] Object deallocated before replying to XPC message."
+ "attributionSignatureForAdDestination"
- "SELECT t.rowid, t.experimentId, t.treatmentId FROM APDBTrigger AS t INNER JOIN APDBExperimentationReport AS er ON er.triggerRowId = t.rowid WHERE er.day = ? AND er.source = ? GROUP BY t.rowid LIMIT %ld OFFSET %ld"

```
