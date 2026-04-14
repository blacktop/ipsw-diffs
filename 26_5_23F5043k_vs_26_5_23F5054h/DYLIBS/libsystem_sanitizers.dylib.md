## libsystem_sanitizers.dylib

> `/usr/lib/system/libsystem_sanitizers.dylib`

```diff

-26.0.0.0.0
-  __TEXT.__text: 0x6340
+26.1.0.0.0
+  __TEXT.__text: 0x62e8
   __TEXT.__auth_stubs: 0x1c0
   __TEXT.__const: 0x160
   __TEXT.__cstring: 0xacc

   - /usr/lib/system/libsystem_malloc.dylib
   - /usr/lib/system/libsystem_platform.dylib
   - /usr/lib/system/libsystem_pthread.dylib
-  UUID: 021030DA-3A92-3EB0-A8F8-BF9360C6D712
+  UUID: FA11BC7D-7B9F-3C53-AD2B-789D34B2346B
   Functions: 207
   Symbols:   455
   CStrings:  133
Functions:
~ __ZN2vm6createIN5trace5DepotILm65536ELm64ELm8EN4hash7Murmur2EXadL_Z16thread_stack_pcsEEEEJEEEPT_DpOT0_ : 176 -> 156
~ __ZN2vm6createIN5trace13AllocationMapILm262144EXadL_ZN4hash7Murmur211hashPointerEmEEEEJEEEPT_DpOT0_ : 164 -> 140
~ __ZN2vm6createIN5trace5DepotILm524288ELm64ELm8EN4hash7Murmur2EXadL_Z16thread_stack_pcsEEEEJEEEPT_DpOT0_ : 176 -> 156
~ __ZN2vm6createIN5trace13AllocationMapILm1048576EXadL_ZN4hash7Murmur211hashPointerEmEEEEJEEEPT_DpOT0_ : 164 -> 140

```
