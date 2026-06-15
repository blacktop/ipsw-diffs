## libsystem_eligibility.dylib

> `/usr/lib/system/libsystem_eligibility.dylib`

```diff

-319.160.10.0.0
-  __TEXT.__text: 0x3a60 sha256:abb27456b3515b840feebcaacb7b8767bbc41a7b9b1c8a218195a4fdff3ca6da
-  __TEXT.__auth_stubs: 0x280 sha256:28c867da1c78eec3be613deb9028a236bf237e2a55a8ae318e5312cbcdf02ecc
-  __TEXT.__const: 0x5b8 sha256:4c0b6fbe6e2c1f9ad2df8c2402fedccb614fb6340c3b90c2eb83a8bfb5567ccf
-  __TEXT.__cstring: 0x4611 sha256:84180f9d985216677148fbdb9907b19f9b63112fd188af953797f38152f7abee
-  __TEXT.__oslogstring: 0x39b sha256:77bc4997012facb33794e7a429b0607d29a3c2aac2e949e8f6e88379b660ca32
-  __TEXT.__unwind_info: 0xb8 sha256:dc976f85cb1921a2f20fcbafd9542214d00400e39fcf7640e86522ab25906c84
+319.160.14.0.0
+  __TEXT.__text: 0x4b08 sha256:dde0a38cd382407989c99d35126d213120887496b4460c2626adb963c98cc005
+  __TEXT.__auth_stubs: 0x280 sha256:7318123d10c345a518c1766a5d42e5e0b1b3083c82e16260f443bbd4f8575824
+  __TEXT.__const: 0x80 sha256:15bb44c3624d993f783de827777a1462be05ece3ad0c04f540bf51506ffc7368
+  __TEXT.__cstring: 0x481d sha256:a752eaec03d7bd47ca3fb02a6f38930be647577abaa2dfdfc1b56041a3adae39
+  __TEXT.__oslogstring: 0x3d6 sha256:b153a83e73e1dae88d9e58e1bc0f64630716ddc199e05f6ae243734b71ed81db
+  __TEXT.__unwind_info: 0xb8 sha256:214d16f1f5a00e081627a3868265b2ee7e093905c7e4718d9190322423fbf632
   __DATA_CONST.__got: 0x28 sha256:2c34ce1df23b838c5abf2a7f6437cca3d3067ed509ff25f11df6b11b582b51eb
-  __DATA_CONST.__const: 0xbb8 sha256:a45f02afaf32d7e6a7aa04d1a401ff4307ef0f9fbca2ba80851960aa75426449
+  __DATA_CONST.__const: 0x828 sha256:7c80b9697aa150048cfcdefa19db7e9614a338b5702b2c77d521f61bf504a7cb
   __AUTH_CONST.__auth_got: 0x140 sha256:7b6436b0c98f62380866d9432c2af0ee08ce16a171bda6951aecd95ee1307d61
-  __AUTH_CONST.__const: 0x40 sha256:75b812a1d521168e417c0234a8dd71eff45a00cc1b9d932280c34067d2d699e3
+  __AUTH_CONST.__const: 0x40 sha256:246ad66db5e7f1e9480d04707e139d697b3c87331169ae7cd351c0a021467a03
   __DATA_DIRTY.__bss: 0x10 sha256:374708fff7719dd5979ec875d56cd2286f6d3cf7ec317a3b25632aab28ec37bb
   - /usr/lib/system/libdispatch.dylib
   - /usr/lib/system/libsystem_blocks.dylib

   - /usr/lib/system/libsystem_malloc.dylib
   - /usr/lib/system/libsystem_trace.dylib
   - /usr/lib/system/libxpc.dylib
-  UUID: 4076ADDB-7CC3-33EF-95AE-B77D075ECA25
-  Functions: 26
+  UUID: 761E44B8-10D8-3A5E-B1EB-50E1C1BD1EB9
+  Functions: 28
   Symbols:   87
-  CStrings:  441
+  CStrings:  449
 
Symbols:
+ ___block_descriptor_tmp.406
- ___block_descriptor_tmp.400
CStrings:
+ "%s: Unsupported domain %llu; falling back to private plist"
+ "OS_ELIGIBILITY_DOMAIN_ADULT_AGE_VERIFICATION_STATUS_REQUIRED_SPYGLASS"
+ "OS_ELIGIBILITY_DOMAIN_UNVERIFIED_ADULT_BACKGROUND_RESTRICTION_REQUIRED"
+ "OS_ELIGIBILITY_DOMAIN_UNVERIFIED_ADULT_BACKGROUND_RESTRICTION_REQUIRED_MINI_BUDDY"
+ "com.apple.os-eligibility-domain.change.adult-age-verification-status-required-spyglass"
+ "com.apple.os-eligibility-domain.change.unverified-adult-background-restriction-required"
+ "com.apple.os-eligibility-domain.change.unverified-adult-background-restriction-required-mini-buddy"
+ "eligibility_domain_to_file"

```
