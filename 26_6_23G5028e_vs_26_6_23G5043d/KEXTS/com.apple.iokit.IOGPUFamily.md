## com.apple.iokit.IOGPUFamily

> `com.apple.iokit.IOGPUFamily`

```diff

-130.16.2.0.0
-  __TEXT.__cstring: 0x5e27 sha256:70f3f5b950249cafd7e94b30eeb5816a3791e899685df27e9b5c27b6afe6dce2
-  __TEXT.__os_log: 0x4bbf sha256:f0116395b0a40a26f838039f2050d3291139ad1e04075c2e85260d65df46680f
+130.16.3.0.0
+  __TEXT.__cstring: 0x5d93 sha256:e98138c7061da7b6d77d71dcc3dbfbc3a49cba53261e0453329a34069601a393
+  __TEXT.__os_log: 0x4c09 sha256:afb9e741db099a66b19136d9b0c28a9fbe156558defc518222fc6a2cbc5a621f
   __TEXT.__const: 0x7c sha256:96419aa1bd138c093f19968e246d0ea061d8653df52c210c4e8b2795d8752a05
-  __TEXT_EXEC.__text: 0x3f9bc sha256:8412d68439ec10e8ce0dcf170753d8c4eab63852de4d57b5c0e840a2ac212274
+  __TEXT_EXEC.__text: 0x40394 sha256:b9b5a36869b1a212d92948c5dbb117110019a0a9dc026fec6e92d2f87c90cb56
   __TEXT_EXEC.__auth_stubs: 0x0
-  __DATA.__data: 0x460 sha256:069bfa73978ce598818dc1fa8a73f558d5fa67c56f5c11d00f4e43fc048a8b88
+  __DATA.__data: 0x460 sha256:cb48c6214c474299697332d29e6417dd22feba0ef266687e76c57ab4c0f54e49
   __DATA.__common: 0x898 sha256:2b63efc11f049529eb9b9876a5396ba3a5af8b73f813836efd844c114bb29834
   __DATA.__bss: 0x9 sha256:3e7077fd2f66d689e0cee6a7cf5b37bf2dca7c979af356d0a31cbc5c85605c7d
-  __DATA_CONST.__auth_got: 0x6c0 sha256:55a41e000857b143d5f24eb776976142835e52396cceb6496cf92a2eefa79663
-  __DATA_CONST.__got: 0x100 sha256:121e2ec79e25497283f7355389c6ef0a846e81a871d73bcc0b79357ce067ae57
-  __DATA_CONST.__auth_ptr: 0x8 sha256:bc327b5d00e16b64f978ecca96f431f3037d95e760c73543f7839c5b817f307c
-  __DATA_CONST.__mod_init_func: 0x100 sha256:c7ef8acdc68bc2eb2745873532f81238a3db637261baff5f84059b767789963d
-  __DATA_CONST.__mod_term_func: 0x100 sha256:157836927d464704a14135454a89333a754bb9b6edc39449be9941f3a75fdbde
-  __DATA_CONST.__const: 0x6f80 sha256:f67836bb8dc470eb7c942e9426811886de8772b98efbd0b18b16e757c46ced4d
-  __DATA_CONST.__kalloc_type: 0x11c0 sha256:10129a335b8928c42eb2bf8ea2c753b9a29dd8a9c17ef69ef4850bc53c13cc0c
-  __DATA_CONST.__kalloc_var: 0x1090 sha256:3cadc11e19cd54e271f98dad34b3f8532067f9d836b2eae6cd99960713209800
-  __DATA_CONST.__assert: 0xa0 sha256:4fee251f2ed04303906b8f6283deae909d0ae60e8aa0a94ed53b8ca23bf7afa3
-  UUID: 0E107FA4-8FB2-35B3-A51D-FCB05A2AC5AF
+  __DATA_CONST.__auth_got: 0x6c0 sha256:6d2d6321b6d6d6acf59e13ac23c96e4fbbf30dcf0a8e28e258417013003771f8
+  __DATA_CONST.__got: 0x100 sha256:46c45ef2eba12ac672ed6cd01ba8ec49a9596e33bad63ca92edc0d535738b377
+  __DATA_CONST.__auth_ptr: 0x8 sha256:65c08b47afaad76e828d7889ec228733f4959f711c0fcfeb9af366f33400adf5
+  __DATA_CONST.__mod_init_func: 0x100 sha256:79d4a25e4c32a35ae92f4c4f176685fc3cad956dbc10dbe97a5b24644f9114b9
+  __DATA_CONST.__mod_term_func: 0x100 sha256:8625ca3c9ca624f9de8329520dc8ab9711cceea9570531f9ea365a7ed861d4bb
+  __DATA_CONST.__const: 0x6f80 sha256:4f60c6ae2f6f4a47a02fe8ad284ccdb8654ee0af512ff711fc969f9c07b5b37d
+  __DATA_CONST.__kalloc_type: 0x11c0 sha256:d7c6e5d2f1174022547526fe138f69c9e9de989cf61296e45475f70dddce4272
+  __DATA_CONST.__kalloc_var: 0x1090 sha256:a30439c8e922140d8361638c0d21a69892c17a5b1404b86df81f912343b1f7a3
+  __DATA_CONST.__assert: 0x28 sha256:7e3d53d35886683c5c06bce55660b7e0711982a6ef1ca8cdd11ff3a992dfc298
+  UUID: 463A291E-4429-3621-B944-DF81D5985C91
   Functions: 1982
   Symbols:   0
-  CStrings:  878
+  CStrings:  877
 
CStrings:
+ "\"Memory object not found in fMemoryCountedSet or fPendingMemorySet\" @%s:%d"
+ "\"Unable to remove just added resource after addMemoryFromResources failure\" @%s:%d"
+ "%s: resource does not own its backing (resType=0x%x child=%u device_cache=%s)\n"
+ "%s: resource does not own its backing (resType=0x%x)\n"
+ "IOGPUSysMemory *IOGPUResource::owns_replaceable_backing() const"
+ "IOReturn IOGPUSysMemory::replace_backing_bytes_locked(task_t, mach_vm_address_t, uint64_t)"
+ "IOReturn IOGPUSysMemory::replace_backing_ranges_locked(task_t, IOAddressRange *, uint32_t, bool)"
+ "NO"
+ "YES"
- "\"Memory object unexpectedly not found in fMemoryCountedSet\" @%s:%d"
- "\"Memory object unexpectedly not found in fPendingMemorySet\" @%s:%d"
- "(numMemoryHashResourcesAdded + numPendingHashResourcesAdded) <= countOfObjectsToAdd"
- "Attempting to detach memory for invalid resource type: %u\n"
- "i == (numMemoryHashResourcesAdded + numPendingHashResourcesAdded)"
- "removedResource == addedResources[i]"
- "result != kIOReturnSuccess"
- "result == kIOReturnSuccess"
- "virtual IOReturn IOGPUSysMemory::replace_backing_bytes(task_t, mach_vm_address_t, uint64_t)"
- "virtual IOReturn IOGPUSysMemory::replace_backing_ranges(task_t, IOAddressRange *, uint32_t, bool)"

```
