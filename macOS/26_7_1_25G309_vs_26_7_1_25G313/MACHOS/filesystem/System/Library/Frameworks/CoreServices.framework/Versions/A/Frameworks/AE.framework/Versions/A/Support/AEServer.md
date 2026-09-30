## AEServer

> `System/Library/Frameworks/CoreServices.framework/Versions/A/Frameworks/AE.framework/Versions/A/Support/AEServer`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__eh_frame`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`

```diff

-982.4.3.0.0
+982.4.4.0.0
   __TEXT.__text: 0x1004c
   __TEXT.__auth_stubs: 0x1000
   __TEXT.__objc_stubs: 0x160

   __TEXT.__const: 0x130
   __TEXT.__gcc_except_tab: 0x38
   __TEXT.__cstring: 0xf0c
-  __TEXT.__oslogstring: 0x1991
+  __TEXT.__oslogstring: 0x19a0
   __TEXT.__objc_classname: 0x20
   __TEXT.__objc_methname: 0xc0
   __TEXT.__objc_methtype: 0xb
CStrings:
+ "%{public}sencryptUserPassword( encypted pw=%{private,hash}s)"
+ "%{public}sencryptUserPassword(pw=%{private,hash}s len=%ld randomSeed=%{private,hash}s)"
- "%{public}sencryptUserPassword( encypted pw=%{private}s)"
- "%{public}sencryptUserPassword(pw=%{private}s len=%ld randomSeed=%{private}s)"
```
