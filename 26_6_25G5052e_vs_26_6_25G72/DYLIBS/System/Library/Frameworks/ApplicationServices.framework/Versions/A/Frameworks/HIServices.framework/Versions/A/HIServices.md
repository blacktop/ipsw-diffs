## HIServices

> `/System/Library/Frameworks/ApplicationServices.framework/Versions/A/Frameworks/HIServices.framework/Versions/A/HIServices`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__cstring`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__dof_Accessibi`
- `__DATA_CONST.__got`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_selrefs`
- `__DATA_CONST.__objc_superrefs`
- `__AUTH_CONST.__auth_got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_const`
- `__AUTH.__data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`

```diff

-817.0.0.0.0
-  __TEXT.__text: 0x5aa84
+818.0.0.0.0
+  __TEXT.__text: 0x5aac0
   __TEXT.__auth_stubs: 0x32a0
   __TEXT.__objc_methlist: 0x10c
   __TEXT.__const: 0x1620

   __TEXT.__ustring: 0xd2
   __TEXT.__gcc_except_tab: 0x358
   __TEXT.__dof_Accessibi: 0x90c
-  __TEXT.__unwind_info: 0xdb8
+  __TEXT.__unwind_info: 0xdc0
   __TEXT.__objc_classname: 0x30
   __TEXT.__objc_methname: 0x4ec
   __TEXT.__objc_methtype: 0xb0

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1852
-  Symbols:   3224
+  Functions: 1853
+  Symbols:   3225
   CStrings:  1309
 
Symbols:
+ UnregisterDragInfo
+ _UnregisterDragInfo
- CoreDragDispose
Functions:
~ _CoreDragCreateInternal : 624 -> 636
~ _CoreDragDispose : 272 -> 220
+ _UnregisterDragInfo
+ GetDragInfo.cold.1
- GetDragInfo.cold.1
CStrings:
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.TGUagR/Sources/HIServices/Accessibility.subproj/Accessibility.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.G0ImSu/Sources/HIServices/Accessibility.subproj/Accessibility.c"
```
