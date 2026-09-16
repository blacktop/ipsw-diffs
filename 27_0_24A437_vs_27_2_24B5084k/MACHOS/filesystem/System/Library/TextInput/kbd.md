## kbd

> `/System/Library/TextInput/kbd`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-3567.0.0.0.0
-  __TEXT.__text: 0xe5d0
-  __TEXT.__auth_stubs: 0x7c0
-  __TEXT.__objc_stubs: 0x2860
+3568.1.4.0.0
+  __TEXT.__text: 0xe70c
+  __TEXT.__auth_stubs: 0x7d0
+  __TEXT.__objc_stubs: 0x28a0
   __TEXT.__objc_methlist: 0x1314
-  __TEXT.__const: 0xd2
+  __TEXT.__const: 0xda
   __TEXT.__objc_classname: 0x53c
-  __TEXT.__objc_methname: 0x340f
+  __TEXT.__objc_methname: 0x3458
   __TEXT.__objc_methtype: 0x12e9
-  __TEXT.__cstring: 0x19e5
-  __TEXT.__oslogstring: 0xbff
+  __TEXT.__cstring: 0x183d
+  __TEXT.__oslogstring: 0xc9b
   __TEXT.__dlopen_cstrs: 0x22c
-  __TEXT.__unwind_info: 0x5b0
-  __DATA_CONST.__const: 0x6e0
+  __TEXT.__unwind_info: 0x5b8
+  __DATA_CONST.__const: 0x728
   __DATA_CONST.__cfstring: 0xae0
   __DATA_CONST.__objc_classlist: 0xb8
   __DATA_CONST.__objc_protolist: 0xf8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x50
   __DATA_CONST.__objc_superrefs: 0x70
-  __DATA_CONST.__auth_got: 0x3e8
+  __DATA_CONST.__auth_got: 0x3f0
   __DATA_CONST.__got: 0x3a0
   __DATA_CONST.__auth_ptr: 0x8
   __DATA.__objc_const: 0x4530
-  __DATA.__objc_selrefs: 0xe28
+  __DATA.__objc_selrefs: 0xe38
   __DATA.__objc_ivar: 0xb8
   __DATA.__objc_data: 0x730
   __DATA.__data: 0xba0

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  Functions: 396
-  Symbols:   252
-  CStrings:  973
+  Functions: 398
+  Symbols:   253
+  CStrings:  970
 
Symbols:
+ _TIInputManagerServerOSLogFacility
CStrings:
+ "Connection interrupted for client PID %{public}d (connection still valid, may resume)"
+ "Connection invalidated for client PID %{public}d (wasInteractingConnection=%{public}d)"
+ "Establishing connection with client PID %{public}d"
+ "Flushing the dynamic resources on inactivity"
+ "Keyboard settings changed. Releasing input managers."
+ "Preparing keyboard for activity"
+ "Preparing keyboard for inactivity"
+ "Preparing keyboard for inactivity, last flush at %lf, flush period: %lf"
+ "Received memory pressure level %ld"
+ "Reduce cache to size=%lu"
+ "releaseAllInputManagersAndLanguageModelResources"
+ "setInterruptionHandler:"
- "%s  Establishing connection with PID %d"
- "%s  Flushing the dynamic resources on inactivity"
- "%s  Keyboard settings changed. Releasing input managers."
- "%s  Preparing keyboard for activity"
- "%s  Preparing keyboard for inactivity"
- "%s  Preparing keyboard for inactivity, last flush at %lf, flush period: %lf"
- "%s  Received memory pressure level %ld"
- "%s  Reduce cache to size=%lu"
- "-[TIKeyboardInputManagerServer appleKeyboardsSettingsChanged:]"
- "-[TIKeyboardInputManagerServer checkAndFlushDynamicCaches]"
- "-[TIKeyboardInputManagerServer handleMemoryPressureLevel:excessMemoryInBytes:]"
- "-[TIKeyboardInputManagerServer listener:shouldAcceptNewConnection:]"
- "-[TIKeyboardInputManagerServer prepareForActivity]"
- "-[TIKeyboardInputManagerServer prepareForInactivity]"
- "-[TIKeyboardInputManagerServer reduceCacheToSize:]"
```
