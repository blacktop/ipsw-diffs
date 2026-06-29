## com.apple.iokit.IOGPUFamily

> `com.apple.iokit.IOGPUFamily`

```diff

-130.14.0.0.0
-  __TEXT.__cstring: 0x5e27 sha256:70f3f5b950249cafd7e94b30eeb5816a3791e899685df27e9b5c27b6afe6dce2
-  __TEXT.__os_log: 0x4bbf sha256:f0116395b0a40a26f838039f2050d3291139ad1e04075c2e85260d65df46680f
+130.15.2.0.0
+  __TEXT.__cstring: 0x5e6c sha256:3a198314543665ef6effa194ad116f3f014d5b16801ca3a4df3e02295c809eb4
+  __TEXT.__os_log: 0x4c09 sha256:afb9e741db099a66b19136d9b0c28a9fbe156558defc518222fc6a2cbc5a621f
   __TEXT.__const: 0x7c sha256:96419aa1bd138c093f19968e246d0ea061d8653df52c210c4e8b2795d8752a05
-  __TEXT_EXEC.__text: 0x3f9b4 sha256:27c1ca672bc9f2b18eb3d7cec508f9a4d8885b4cf8658bf6e73358b5b39ab48f
+  __TEXT_EXEC.__text: 0x3fbbc sha256:68c4d87eb63789431e76e75aabdd3637fb3040db881d9866dd94df37b4f20341
   __TEXT_EXEC.__auth_stubs: 0x0
-  __DATA.__data: 0x460 sha256:73a5cbc81e158195e6f42b7c5789659b0e8f6eebe46e0c0d59a7dc56f6ff3fa4
+  __DATA.__data: 0x460 sha256:9973ee88502abccbc4806cd70ded1e655790d0eb0cd03faba7e80eb6ba6526bf
   __DATA.__common: 0x898 sha256:2b63efc11f049529eb9b9876a5396ba3a5af8b73f813836efd844c114bb29834
   __DATA.__bss: 0x9 sha256:3e7077fd2f66d689e0cee6a7cf5b37bf2dca7c979af356d0a31cbc5c85605c7d
-  __DATA_CONST.__auth_got: 0x6c0 sha256:88180178b449523671ab46b3e715a2b75f0a4bc921e79b4a43df4ef210061a0a
-  __DATA_CONST.__got: 0x100 sha256:f590752dadbb777f59130dd5eba0a380f4c6e493f6ac239e82be1099c57766ea
-  __DATA_CONST.__auth_ptr: 0x8 sha256:bf6ec49501e3d3040672c70ea50ab65eaa2eef4728b3363a17ff6bb8037bd37e
-  __DATA_CONST.__mod_init_func: 0x100 sha256:0eef02e94f754be950c5f8c7734348ba088413c68d81f286a557714cf9d0e26d
-  __DATA_CONST.__mod_term_func: 0x100 sha256:3a10d3f338bdd160e0d639599971c17d309409cc36740da914b05acf45d8739b
-  __DATA_CONST.__const: 0x6f80 sha256:2a602584dc96479f1fc4f1aa407fa2854e5fc864f23ef31866d70938b9ab1e16
-  __DATA_CONST.__kalloc_type: 0x11c0 sha256:6d97b016f2f83a0c9a7bf6c52b7b9d05085424c34d00ac0e16407576296052db
-  __DATA_CONST.__kalloc_var: 0x1090 sha256:5c1bee4e841945fc474842f3fca35a7da9f8e904a932683632e25281c736eac3
-  __DATA_CONST.__assert: 0xa0 sha256:b7ce5e845e47a1afa883d12acae247218016de1ef3cf8d601818569dc9a56385
-  UUID: 77CCB658-4E6A-30BD-83E9-5EB437305A07
-  Functions: 1982
+  __DATA_CONST.__auth_got: 0x6c0 sha256:4b19d9986fc11fae92795816f945bab5236230feb9e36612d237198fac969c7b
+  __DATA_CONST.__got: 0x100 sha256:d10a150ea807dd49db9ed90996086495aee1561882d3452d85cb3fa7bd5daa8f
+  __DATA_CONST.__auth_ptr: 0x8 sha256:222e57fcbcf953060ae8b62393809d79531543463531902cfe54ab3b990f7466
+  __DATA_CONST.__mod_init_func: 0x100 sha256:fd23f474eca59cab8da06be8b334965fc4a46f7a39738697d96dae32aa3e60b7
+  __DATA_CONST.__mod_term_func: 0x100 sha256:9e40d06d4773f8b175b9d4a807d571b715bf800786f905e3f897f548168d71a1
+  __DATA_CONST.__const: 0x6f80 sha256:decc7f19b4efb0d082c7107442f3771c77398346c07bf984c424cc526e330f1b
+  __DATA_CONST.__kalloc_type: 0x11c0 sha256:215cdf23de3ef09ee03ad5cf72f4ad8298d8214b37df321e239da0e29a8d5a99
+  __DATA_CONST.__kalloc_var: 0x1090 sha256:7aa4d2ac6e0da92e58d33a8eda26697e7e8a90f93bfa58245e3956fa1ad439f1
+  __DATA_CONST.__assert: 0xa0 sha256:e95b312d39a30ddd30c2037a4aaaaa0803899a599575f19fca27f2f153b338c5
+  UUID: B6991C68-E985-34D4-BA93-070AD33A7319
+  Functions: 1987
   Symbols:   0
-  CStrings:  878
+  CStrings:  882
 
CStrings:
+ "%s: resource does not own its backing (resType=0x%x child=%u device_cache=%s)\n"
+ "%s: resource does not own its backing (resType=0x%x)\n"
+ "IOGPUSysMemory *IOGPUResource::owns_replaceable_backing() const"
+ "IOReturn IOGPUSysMemory::replace_backing_bytes_locked(task_t, mach_vm_address_t, uint64_t)"
+ "IOReturn IOGPUSysMemory::replace_backing_ranges_locked(task_t, IOAddressRange *, uint32_t, bool)"
+ "NO"
+ "YES"
- "Attempting to detach memory for invalid resource type: %u\n"
- "virtual IOReturn IOGPUSysMemory::replace_backing_bytes(task_t, mach_vm_address_t, uint64_t)"
- "virtual IOReturn IOGPUSysMemory::replace_backing_ranges(task_t, IOAddressRange *, uint32_t, bool)"

```
