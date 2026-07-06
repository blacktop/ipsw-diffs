## com.apple.tailspin

> `/System/Library/UserEventPlugins/com.apple.tailspin.plugin/Contents/MacOS/com.apple.tailspin`

```diff

-  __TEXT.__text: 0x644
+  __TEXT.__text: 0x64c
   __TEXT.__auth_stubs: 0x1e0
   __TEXT.__objc_stubs: 0xa0
   __TEXT.__const: 0x58
   __TEXT.__cstring: 0x8c
-  __TEXT.__oslogstring: 0xfe
+  __TEXT.__oslogstring: 0x11c
   __TEXT.__objc_methname: 0x5a
   __TEXT.__unwind_info: 0x78
   __DATA.__const: 0x48
Sections:
~ __TEXT.__const : content changed
~ __TEXT.__unwind_info : content changed
~ __DATA.__const : content changed
~ __DATA.__objc_selrefs : content changed
Functions:
~ _init_tailspin : 1192 -> 1200
CStrings:
+ "%{public}s reset on-disk tailspin configuration. Apple-Internal: %{bool}d, Is Photos: %{bool}d, Is tailspind 300MB: %{bool}d"
- "%{public}s reset on-disk tailspin configuration. Apple-Internal: %{bool}d, Is Photos: %{bool}d"

```
