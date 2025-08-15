## remindd

> `/usr/libexec/remindd`

```diff

-1041.0.0.0.0
-  __TEXT.__text: 0x74fa60
-  __TEXT.__auth_stubs: 0x5570
+1046.0.0.0.0
+  __TEXT.__text: 0x74ffd0
+  __TEXT.__auth_stubs: 0x5580
   __TEXT.__objc_stubs: 0xf9a0
   __TEXT.__objc_methlist: 0x87a8
-  __TEXT.__const: 0x1e714
+  __TEXT.__const: 0x1e724
   __TEXT.__objc_methname: 0x210e6
   __TEXT.__objc_classname: 0x149c
   __TEXT.__objc_methtype: 0x3638
   __TEXT.__gcc_except_tab: 0x1aa4
-  __TEXT.__cstring: 0x5aca0
+  __TEXT.__cstring: 0x5ae90
   __TEXT.__oslogstring: 0x1a52a
   __TEXT.__swift5_entry: 0x8
   __TEXT.__swift5_typeref: 0x12490
-  __TEXT.__swift5_fieldmd: 0x917c
+  __TEXT.__swift5_fieldmd: 0x9188
   __TEXT.__constg_swiftt: 0xaae0
   __TEXT.__swift5_builtin: 0x320
-  __TEXT.__swift5_reflstr: 0xad4d
+  __TEXT.__swift5_reflstr: 0xad7d
   __TEXT.__swift5_assocty: 0x1c60
   __TEXT.__swift5_capture: 0x5cb4
   __TEXT.__swift5_protos: 0x23c
   __TEXT.__swift5_proto: 0x150c
   __TEXT.__swift5_types: 0x954
   __TEXT.__swift5_mpenum: 0xac
-  __TEXT.__unwind_info: 0x121e0
+  __TEXT.__unwind_info: 0x12068
   __TEXT.__eh_frame: 0x1ddf8
-  __DATA_CONST.__auth_got: 0x2ac8
+  __DATA_CONST.__auth_got: 0x2ad0
   __DATA_CONST.__got: 0x1818
   __DATA_CONST.__auth_ptr: 0x988
   __DATA_CONST.__const: 0x20ae0

   __DATA_CONST.__objc_arrayobj: 0x270
   __DATA_CONST.__objc_dictobj: 0x140
   __DATA_CONST.__objc_doubleobj: 0x20
-  __DATA.__objc_const: 0x1d818
+  __DATA.__objc_const: 0x1d838
   __DATA.__objc_selrefs: 0x73e0
   __DATA.__objc_ivar: 0x42c
   __DATA.__objc_data: 0x7bf0

   - /System/Library/PrivateFrameworks/UnifiedAssetFramework.framework/UnifiedAssetFramework
   - /System/Library/PrivateFrameworks/UserManagement.framework/UserManagement
   - /System/Library/PrivateFrameworks/iCalendar.framework/iCalendar
+  - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 9535046B-45CC-33A9-A501-860FC5F1CFE0
-  Functions: 26010
-  Symbols:   2815
-  CStrings:  12183
+  UUID: 3A283415-2D9D-31E6-824C-F279BCC6F22A
+  Functions: 26012
+  Symbols:   2816
+  CStrings:  12188
 
Symbols:
+ _MGCopyAnswer
CStrings:
+ "$__lazy_storage_$_shouldRunClassifierOnBuild"
+ "%{public}s: Skipped auto-categorizing reminder {listObjectID: %{public}@, reminderIdentifier: %{public}s, sectionIdentifier: %{public}s, shouldUpdateGroceryLocalCorrections: %{bool,public}d}"
+ "%{public}s: The grocery classifier operation is currently disabled on this device"
+ "RDGroceryOperationCategorizeRemindersInList: Running on hardware %s"
+ "RDGroceryOperationCategorizeRemindersInList: cannot read hardware name"

```
