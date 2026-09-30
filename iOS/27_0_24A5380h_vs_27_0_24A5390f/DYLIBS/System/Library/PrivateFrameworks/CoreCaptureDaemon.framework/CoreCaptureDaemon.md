## CoreCaptureDaemon

> `/System/Library/PrivateFrameworks/CoreCaptureDaemon.framework/CoreCaptureDaemon`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__weak_got`
- `__DATA_CONST.__objc_selrefs`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__weak_auth_got`

```diff

-1355.42.0.0.0
-  __TEXT.__text: 0x5b998
+1355.44.0.0.0
+  __TEXT.__text: 0x5bac0
   __TEXT.__const: 0x638
   __TEXT.__gcc_except_tab: 0x4d4
-  __TEXT.__oslogstring: 0xb71b
-  __TEXT.__cstring: 0xbb5e
+  __TEXT.__oslogstring: 0xb77d
+  __TEXT.__cstring: 0xbbc0
   __TEXT.__unwind_info: 0x7d0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   - /usr/lib/libz.1.dylib
   Functions: 615
   Symbols:   1166
-  CStrings:  1237
+  CStrings:  1238
 
Functions:
~ __ZN8CCLogTap11tapLoopImplEv : 3640 -> 3936
CStrings:
+ "CCLogTap::tapLoopImpl() entry:%u failed to map pipe with rc[0x%08x] ringSize[%llu]\n"
+ "CCLogTap::tapLoopImpl() entry:%u failed to unmap zero-length pipe with rc[0x%08x]\n"
- "CCLogTap::tapLoopImpl() entry:%u failed to map pipe with rc[0x%08x]\n"
```
