## AppStoreComponentsDaemonKit

> `/System/Library/PrivateFrameworks/AppStoreComponentsDaemonKit.framework/AppStoreComponentsDaemonKit`

### Sections with Same Size but Changed Content

- `__TEXT.__cstring`

```diff

-27.2.5.2.1
-  __TEXT.__text: 0x113820
-  __TEXT.__objc_methlist: 0x49c4
+27.2.10.0.0
+  __TEXT.__text: 0x1145c4
+  __TEXT.__objc_methlist: 0x4a0c
   __TEXT.__const: 0x79e0
   __TEXT.__cstring: 0x736c
-  __TEXT.__oslogstring: 0x1e99
+  __TEXT.__oslogstring: 0x1ecd
   __TEXT.__gcc_except_tab: 0x58
   __TEXT.__dlopen_cstrs: 0x8e
   __TEXT.__constg_swiftt: 0x1c20
   __TEXT.__swift5_typeref: 0x37f7
-  __TEXT.__swift5_fieldmd: 0x1838
+  __TEXT.__swift5_fieldmd: 0x1844
   __TEXT.__swift5_builtin: 0x1f4
-  __TEXT.__swift5_reflstr: 0x1330
+  __TEXT.__swift5_reflstr: 0x1340
   __TEXT.__swift5_assocty: 0x7e8
   __TEXT.__swift5_capture: 0x1b98
   __TEXT.__swift5_proto: 0x4b8

   __TEXT.__swift_as_cont: 0x5bc
   __TEXT.__swift5_mpenum: 0x24
   __TEXT.__swift5_protos: 0x48
-  __TEXT.__unwind_info: 0x48c0
-  __TEXT.__eh_frame: 0x8804
+  __TEXT.__unwind_info: 0x48d0
+  __TEXT.__eh_frame: 0x87fc
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x1d0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1f50
+  __DATA_CONST.__objc_selrefs: 0x1f60
   __DATA_CONST.__objc_protorefs: 0x148
   __DATA_CONST.__objc_superrefs: 0x1f8
   __DATA_CONST.__got: 0xd50
   __AUTH_CONST.__const: 0x6478
   __AUTH_CONST.__cfstring: 0x3820
-  __AUTH_CONST.__objc_const: 0xa6f0
-  __AUTH_CONST.__auth_got: 0x2048
+  __AUTH_CONST.__objc_const: 0xa760
+  __AUTH_CONST.__auth_got: 0x2068
   __AUTH.__objc_data: 0xc00
   __AUTH.__data: 0x3b0
   __DATA.__objc_ivar: 0x3cc

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 4765
-  Symbols:   4066
-  CStrings:  1072
+  Functions: 4770
+  Symbols:   4073
+  CStrings:  1073
 
Symbols:
+ +[ASCMobileGestalt hwModelDescriptionForUserVisibility]
+ +[ASCMobileGestalt productTypeDescForUserVisibility]
+ -[ASCJSClientObject checkEligibilityDomain:contextDictionary:]
+ -[ASCJSClientObject hwModelDescriptionForUserVisibility]
+ -[ASCJSClientObject productTypeDescForUserVisibility]
+ _MobileGestalt_copy_hwModelDescriptionForUserVisibility_obj
+ _MobileGestalt_copy_productTypeDescForUserVisibility_obj
+ _MobileGestalt_get_current_device
- -[ASCJSClientObject _checkEligibilityDomain:withContextDictionary:]
CStrings:
+ "98E7088B-9F27-4E8A-B59E-2DFE18DF60F4"
+ "Tried to query eligibility but domain %{public}@ is invalid"
+ "Tried to query eligibility without a domain"
- ": blocked by App Store restrictions"
- "Tried to query eligibility but domain %@ is invalid"
```
