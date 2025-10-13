## mmaintenanced

> `/usr/libexec/mmaintenanced`

```diff

-207.0.0.0.0
-  __TEXT.__text: 0x20068
+210.0.0.0.0
+  __TEXT.__text: 0x200b4
   __TEXT.__auth_stubs: 0x1320
   __TEXT.__init_offsets: 0x8
-  __TEXT.__oslogstring: 0x29d1
+  __TEXT.__oslogstring: 0x29e1
   __TEXT.__const: 0x12d0
   __TEXT.__cstring: 0x1be4
   __TEXT.__gcc_except_tab: 0x8c0

   - /usr/lib/swift/libswift_DarwinFoundation1.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 5F4E7617-53C9-3355-B0B0-8C2497637E75
+  UUID: 508B8536-0F47-39C0-BD84-32610B9D75DE
   Functions: 646
   Symbols:   3507
   CStrings:  465
Functions:
~ __Z24get_named_bytes_by_regexP16mach_memory_infojRKNSt3__111basic_regexIcNS1_12regex_traitsIcEEEE : 232 -> 244
~ __Z32current_pressure_level_correctedRj : 1172 -> 1236
CStrings:
+ "com.apple.driver.AppleH[0-9]+CameraInterface.NonPersistent.*"
+ "pressure: raw level %u -> corrected %u, excluded bytes %llu of which collectable %llu, diag %llu, mte tags %llu, kext site %llu, kext named %llu"
- "com.apple.driver.AppleH[0-9]+CameraInterface.NonPersistent"
- "pressure: raw level %u -> corrected %u, excluded bytes %llu of which collectable %llu, diag %llu, kext site %llu, kext named %llu"

```
