## com.apple.driver.IOPAudioSpeaker

> `com.apple.driver.IOPAudioSpeaker`

```diff

-940.17.0.0.0
+1000.40.0.0.0
   __TEXT.__const: 0x18 sha256:7f0eab27d30359d26f30c139f26b5aa5fe664489567a309b4a67bfa19203d869
-  __TEXT.__cstring: 0x19e sha256:7a73eacb78c0774f7b738cc4af9b16251ecef78d2f7b5f6886400f0467968789
-  __TEXT.__os_log: 0x8b sha256:d1907ed491b7593f0d2a96861d1e3c23d04379a6c107f208c19a13c49795ce17
-  __TEXT_EXEC.__text: 0x15d4 sha256:dd21ae02cd39133af02a19d20386145ef93557ed4da94a21618da520f13653ba
+  __TEXT.__cstring: 0x4c3 sha256:bf3628801545be967001c75c89e044cca7815863dd3a3b1e4acfcd5c95af5201
+  __TEXT.__os_log: 0x1ae sha256:661eeb3f6eb75be3d241a1629f32908dc79be18aa402a6114b3ce427ae8f0db7
+  __TEXT_EXEC.__text: 0x2358 sha256:ac4199f3ae0ca7e64456bb842dc774f8ea62c0ece69b255b065b0fab468342e1
   __TEXT_EXEC.__auth_stubs: 0x0
-  __DATA.__data: 0xc8 sha256:c2e0e47bdf7a2b483ce0148e257696331d4a6126a5d760ea5a54d2e7e9d73948
+  __DATA.__data: 0xc8 sha256:ace1f586484eb79ac21d71bdec57350d59f40e58e13aca4410b68f0ff1ca0d38
   __DATA.__common: 0x38 sha256:d4817aa5497628e7c77e6b606107042bbba3130888c5f47a375e6179be789fbb
-  __DATA_CONST.__auth_got: 0x88 sha256:b8170645da29bf20da055dfeb518f4e748cda677b5785bb2078678c0ef04389f
-  __DATA_CONST.__got: 0x48 sha256:06c5e0a7e6bc8f07eb8208b712ad3c9e9a1f666d6b4d58edec79a0296c5fa614
-  __DATA_CONST.__mod_init_func: 0x8 sha256:b125edaafa2356fffac13bfc1581ed5a54c63bb8e3de8a8b56f3e101daa0eb22
-  __DATA_CONST.__mod_term_func: 0x8 sha256:005483889f8ec619b85d9cf3280ddfb1ecf3c7334cf4b43b304a64e4f0e924d8
-  __DATA_CONST.__const: 0xb68 sha256:6a6e2a13acce8406e2c66d17c472b3eb0c69cbb513bbbd029b1d3b2531c472ee
-  __DATA_CONST.__kalloc_type: 0x40 sha256:c343f21e0f41b99b95b8f601d8ade13ad9a00728ed13f3515b146f98e16929da
-  UUID: 0A91E341-B180-39F2-A213-6F61F082E0B7
-  Functions: 56
+  __DATA_CONST.__mod_init_func: 0x8 sha256:b0379045bb33ac6109a5d9ea57aaaff3362586769a2600295af578ed88e02a6d
+  __DATA_CONST.__mod_term_func: 0x8 sha256:0b2638c0d0ae307b97cc8bd05d4a11eb8e61024acd8f9b6b81eded0907ca63a5
+  __DATA_CONST.__const: 0xb70 sha256:361e3146d6ec3888a5276b018cff8b88ed64873cc50d8086e00cfe17eacdaa34
+  __DATA_CONST.__kalloc_type: 0x40 sha256:57801ff22364b51cad3e61dacb1ff5d58f52dcf4329b6af4b125a7a58e19c1ef
+  __DATA_CONST.__auth_got: 0xa8 sha256:310a29f75bbc64cec07907ce52a82cbf389ffc8f83d6e5a5590e0d0361a1037e
+  __DATA_CONST.__got: 0x48 sha256:845c6199c2e7633e9776bd6bdaffcd69bbf75b4738b78b080f8ce8d06c4cd649
+  UUID: 78AC3E92-F03D-3149-A3CA-079F81CFED8C
+  Functions: 65
   Symbols:   0
-  CStrings:  23
+  CStrings:  40
 
CStrings:
+ "\"%s\" @%s:%d"
+ "%s::%s line:%d inDirection:%u"
+ "%s::%s line:%d inDirection:%u outCurrentBitsPerSample=%u ret=%d"
+ "%s::%s() ByteOffset=%d, nodeID %c%c%c%c, propertyID %d edtKeyName:%s\n"
+ "%s::%s() failed to transfer node %c%c%c%c, propertyId %u, ret = %x\n"
+ "%s::%s() failed to transfer node %c%c%c%c, propertyId %u, ret = %x\n\n"
+ "%s::%s() node %c%c%c%c, propertyId %u propertyVal is NULL\n"
+ "%s::%s() node %c%c%c%c, propertyId %u propertyVal is NULL\n\n"
+ "OSBoundedPtr.h"
+ "The offset of the pointer inside its valid memory range can't be represented using int32_t"
+ "The range of valid memory is too large to be represented by this type, or [begin, end) is not a well-formed range"
+ "This bounded_ptr is pointing to memory outside of what can be represented by a native pointer."
+ "bounded_ptr<T>::discard_bounds: Discarding the bounds on this pointer would lose the fact that it is outside of the bounds set originally"
+ "bounded_ptr<T>::operator+=(n): Adding the specified number of bytes to the offset representing the current position would overflow."
+ "device-property-list"
+ "getSupportedBitsPerSampleList"
+ "transferEdtDeviceProperties"

```
