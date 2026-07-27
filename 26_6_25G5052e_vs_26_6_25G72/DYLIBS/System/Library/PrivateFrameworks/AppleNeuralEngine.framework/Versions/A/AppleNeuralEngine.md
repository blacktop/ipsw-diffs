## AppleNeuralEngine

> `/System/Library/PrivateFrameworks/AppleNeuralEngine.framework/Versions/A/AppleNeuralEngine`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__cstring`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__got`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_selrefs`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__AUTH_CONST.__auth_got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_const`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH.__objc_data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`
- `__DATA_DIRTY.__data`

```diff

-380.601.0.0.0
-  __TEXT.__text: 0x4b4fc
+380.700.0.0.0
+  __TEXT.__text: 0x4b51c
   __TEXT.__auth_stubs: 0xa00
   __TEXT.__objc_methlist: 0x264c
   __TEXT.__const: 0x288
Functions:
~ -[_ANEIOSurfaceOutputSets initWithstatsSurRef:outputBuffer:] : 168 -> 176
~ -[_ANEIOSurfaceOutputSets dealloc] : 56 -> 80
CStrings:
+ "%@: { statsSurRef=%p ; outputBuffer=%@}"
- "%@: { statsSurRef=%@ ; outputBuffer=%@}"
```
