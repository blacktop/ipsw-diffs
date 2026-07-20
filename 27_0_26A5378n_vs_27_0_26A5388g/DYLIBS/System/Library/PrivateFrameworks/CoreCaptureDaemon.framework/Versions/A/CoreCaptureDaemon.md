## CoreCaptureDaemon

> `/System/Library/PrivateFrameworks/CoreCaptureDaemon.framework/Versions/A/CoreCaptureDaemon`

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

-1345.39.0.0.0
-  __TEXT.__text: 0x5c200
+1345.42.0.0.0
+  __TEXT.__text: 0x5c328
   __TEXT.__const: 0x63e
   __TEXT.__gcc_except_tab: 0x4a8
-  __TEXT.__oslogstring: 0xba48
-  __TEXT.__cstring: 0xbe6a
+  __TEXT.__oslogstring: 0xbaaa
+  __TEXT.__cstring: 0xbecc
   __TEXT.__unwind_info: 0x810
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   - /usr/lib/libz.1.dylib
   Functions: 632
   Symbols:   1193
-  CStrings:  1251
+  CStrings:  1252
 
Functions:
~ __ZN8CCLogTap11tapLoopImplEv : 3640 -> 3936
CStrings:
+ "CCLogTap::tapLoopImpl() entry:%u failed to map pipe with rc[0x%08x] ringSize[%llu]\n"
+ "CCLogTap::tapLoopImpl() entry:%u failed to unmap zero-length pipe with rc[0x%08x]\n"
- "CCLogTap::tapLoopImpl() entry:%u failed to map pipe with rc[0x%08x]\n"
```
