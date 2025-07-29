## NTKCustomization

> `/System/Library/NanoPreferenceBundles/Customization/NTKCustomization.bundle/NTKCustomization`

```diff

-2393.3.0.0.0
-  __TEXT.__text: 0x10094
-  __TEXT.__auth_stubs: 0x7b0
-  __TEXT.__objc_stubs: 0x3e80
+2398.27.0.0.0
+  __TEXT.__text: 0x10300
+  __TEXT.__auth_stubs: 0x7c0
+  __TEXT.__objc_stubs: 0x3ec0
   __TEXT.__objc_methlist: 0xdf8
   __TEXT.__const: 0x128
-  __TEXT.__gcc_except_tab: 0x2e8
-  __TEXT.__objc_methname: 0x5906
-  __TEXT.__cstring: 0xaaf
-  __TEXT.__oslogstring: 0xbfb
+  __TEXT.__gcc_except_tab: 0x2e4
+  __TEXT.__objc_methname: 0x592c
+  __TEXT.__cstring: 0xaf8
+  __TEXT.__oslogstring: 0xbf9
   __TEXT.__objc_classname: 0x2db
   __TEXT.__objc_methtype: 0x1d6c
-  __TEXT.__unwind_info: 0x49c
-  __DATA_CONST.__auth_got: 0x3e8
-  __DATA_CONST.__got: 0x148
-  __DATA_CONST.__const: 0x708
-  __DATA_CONST.__cfstring: 0xac0
+  __TEXT.__unwind_info: 0x4b8
+  __DATA_CONST.__auth_got: 0x3f0
+  __DATA_CONST.__got: 0x150
+  __DATA_CONST.__const: 0x730
+  __DATA_CONST.__cfstring: 0xb00
   __DATA_CONST.__objc_classlist: 0x60
   __DATA_CONST.__objc_protolist: 0x78
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_arraydata: 0x30
   __DATA_CONST.__objc_dictobj: 0x50
   __DATA.__objc_const: 0x4598
-  __DATA.__objc_selrefs: 0x1288
-  __DATA.__objc_classrefs: 0x2c0
+  __DATA.__objc_selrefs: 0x1298
+  __DATA.__objc_classrefs: 0x2c8
   __DATA.__objc_superrefs: 0x58
   __DATA.__objc_ivar: 0xfc
   __DATA.__objc_data: 0x3c0

   - /System/Library/PrivateFrameworks/Preferences.framework/Preferences
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 7ED32E13-FBEE-392D-8ECC-FD2C15F77AD2
-  Functions: 357
-  Symbols:   303
-  CStrings:  1365
+  UUID: 4F4F3B68-2380-37EA-8C0D-D9F2F6D5FAE3
+  Functions: 356
+  Symbols:   307
+  CStrings:  1372
 
Symbols:
+ _CFAbsoluteTimeGetCurrent
+ _NSStringFromCGSize
+ _NTKFaceSnapshotRendererSuccessLogMessage
+ _OBJC_CLASS_$_NSError
+ _kNTKFaceSnapshotRendererErrorDomain
- _objc_retain_x25
CStrings:
+ " hasBlankComplication"
+ "%.2f seconds - %@: %@ %@"
+ "%.2f seconds - snapshot failed: %@, error: %@"
+ "errorWithDomain:code:userInfo:"
+ "finalizeForSnapshotting completed after timeout"
+ "finalizeForSnapshotting failed after timeout: %@"
+ "preform prewarm routine finished after timeout"
+ "size"
+ "size=%@ hasBlankComplication=%d"
+ "snapshot failed: %@"
+ "snapshot succeeded%@"
+ "v24@?0@\"UIImage\"8@\"NSError\"16"
- "Creating view for snapshotting face %@"
- "Telling view snapshotting is happening"
- "Took snapshot for face (%@)"
- "error finalizing for snapshot: %@"
- "success=%d hasBlankComplications=%d"
- "timeout out waiting for view to finalize for snapshotting"
- "view finalized after we timed out!"

```
