## AppStoreComponents

> `/System/Library/PrivateFrameworks/AppStoreComponents.framework/AppStoreComponents`

### Sections with Same Size but Changed Content

- `__TEXT.__cstring`

```diff

-27.1.7.0.0
-  __TEXT.__text: 0x8ce44
-  __TEXT.__objc_methlist: 0x8c3c
+27.1.11.0.0
+  __TEXT.__text: 0x8cebc
+  __TEXT.__objc_methlist: 0x8c54
   __TEXT.__const: 0x2394
   __TEXT.__cstring: 0x3921
-  __TEXT.__oslogstring: 0x3214
+  __TEXT.__oslogstring: 0x3226
   __TEXT.__gcc_except_tab: 0x8f0
   __TEXT.__dlopen_cstrs: 0x14f
   __TEXT.__constg_swiftt: 0x82c

   __TEXT.__swift5_types: 0xc4
   __TEXT.__swift5_protos: 0xc
   __TEXT.__swift5_capture: 0x200
-  __TEXT.__unwind_info: 0x3258
+  __TEXT.__unwind_info: 0x3260
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_catlist: 0x50
   __DATA_CONST.__objc_protolist: 0x148
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3ef0
+  __DATA_CONST.__objc_selrefs: 0x3f00
   __DATA_CONST.__objc_protorefs: 0x38
   __DATA_CONST.__objc_superrefs: 0x430
   __DATA_CONST.__objc_arraydata: 0x80
   __DATA_CONST.__got: 0x920
   __AUTH_CONST.__const: 0x1ef8
   __AUTH_CONST.__cfstring: 0x4ce0
-  __AUTH_CONST.__objc_const: 0xfa98
+  __AUTH_CONST.__objc_const: 0xfac8
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__objc_doubleobj: 0x80
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__auth_got: 0xd40
   __AUTH.__objc_data: 0x11b8
   __AUTH.__data: 0x5d8
-  __DATA.__objc_ivar: 0x884
+  __DATA.__objc_ivar: 0x888
   __DATA.__data: 0x20e8
   __DATA.__common: 0x160
   __DATA_DIRTY.__objc_data: 0x1c20

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 3821
-  Symbols:   5959
+  Functions: 3823
+  Symbols:   5962
   CStrings:  973
 
Symbols:
+ -[ASCLockupView hiddenReason]
+ -[ASCLockupView setHiddenReason:]
+ _OBJC_IVAR_$_ASCLockupView._hiddenReason
Functions:
~ -[ASCLockupView setLockupSize:] : 148 -> 200
~ -[ASCLockupView setHidden:] : 92 -> 8
+ -[ASCLockupView setHiddenReason:]
+ -[ASCLockupView setWebBrowserFlowType:]
CStrings:
+ ":"
+ "Current process is not eligible to use %{public}@ lockup view size, keeping %{public}@ and hiding lockup"
- "*"
- "Current process is not eligible to use %{public}@ lockup view size, keeping %{public}@"
```
