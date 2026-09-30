## com.apple.driver.AppleBasebandM20

> `com.apple.driver.AppleBasebandM20`

```diff

-1114.0.0.0.0
+1115.0.0.0.0
   __TEXT.__const: 0x39d sha256:39515daf3ac3cb9808d25c373e1b6a4ae04ae009233ff4d14252ffaf430fb65a
-  __TEXT.__cstring: 0xa534 sha256:5deebe3f63e837f1dfb185adde664f8b5812993ee8ce37fc45e27ef4e3ae127d
-  __TEXT.__os_log: 0x9998 sha256:bc53714ed3615d29d194c4a38b78fde5c06fbef329aca95a932bc097f7e54549
-  __TEXT_EXEC.__text: 0x49784 sha256:5c6cabf00403ae5e2c19fbcded2591ae23589380aebddb5d8299afecf8fb1b05
-  __TEXT_EXEC.__auth_stubs: 0x0
-  __DATA.__data: 0x1d8 sha256:ccf1173d53e68a85b4985034e17ef135178ae146a4b45660598619893fe640ba
+  __TEXT.__cstring: 0xa6b4 sha256:7898f7b15374326519437b4fc1622b857f49ada3f6e7c6f899fb28d63fda3348
+  __TEXT.__os_log: 0x9aeb sha256:af3851e86a8bd3a70f22ca86697e08019faf7ca989fc82d622eb692abb426493
+  __TEXT_EXEC.__text: 0x49cb0 sha256:9a577c4a96055baff9e23a273f96ced53294e576a3c5d3c030d137bf7a35d49d
+  __TEXT_EXEC.__auth_stubs: 0x580 sha256:224666a1b430cfe004f88cd5024f3e18ff74b5112872b7e1a8b074176fbab02f
+  __DATA.__data: 0x1f0 sha256:18f691664e721127b039ded42c474e13d226aa0e6e79e8cf5ab804a0f0fb84ed
   __DATA.__common: 0x2c8 sha256:283de789c3f9ae6115e627ecb921b7b39bdaa1b82289eca5e60da0b76d07a502
   __DATA.__bss: 0x2d1 sha256:0782dfda506cb45fd2541d473b203e3902e9affb4eae0c4dbf4e9b10b792e71f
-  __DATA_CONST.__mod_init_func: 0x90 sha256:ef3f7ad8890edbb6fdc45276d375072b5027259d90fa241023127b29cc2a482a
-  __DATA_CONST.__mod_term_func: 0x90 sha256:82da31440b3ff70a19957882935ead419a5005b6448a5776c599e69bbc0b5677
-  __DATA_CONST.__const: 0x6418 sha256:248648b06e8ee42131099efd21da989f6f56bd49c44851336132d3c35512f6e8
-  __DATA_CONST.__kalloc_type: 0x580 sha256:19a0439d532f8848c533d6b032a5ef03dcb61b81ab05598a43e5f4dbb489d7df
-  __DATA_CONST.__kalloc_var: 0x3c0 sha256:30e2fdb3d610dcdf52684a0ec07dc8d17749c7eca10c8c55ab8b3d535550d56f
-  __DATA_CONST.__auth_got: 0x2c0 sha256:b8c9ce45f8ef0559e405a5dbcbf848cb548f5d8bd9fde8cdfd75e42ae2ba2a7c
-  __DATA_CONST.__got: 0xb8 sha256:c79653df379f86a90ea2b3f3792966ea23239ad7990af1550e06261cf3dbe9ce
-  UUID: 6B570852-C62A-3F6E-87BC-D0129F5563FB
-  Functions: 843
+  __DATA_CONST.__mod_init_func: 0x90 sha256:b5dd3e9a35bd5437f5ada07b750fd2f10e421259f56acb71629b001cd601e196
+  __DATA_CONST.__mod_term_func: 0x90 sha256:acc5d6e0965171183da2f72fbed25631d297613a43a8e72551ad64bc37d2ab7b
+  __DATA_CONST.__const: 0x6418 sha256:17ce3a92a08b31982e8f18af5a143bebda0b971d26941bc13889e2bf306d8ade
+  __DATA_CONST.__kalloc_type: 0x580 sha256:2eb692475c4d4adf7b4bbe62d65782b59fd072af6aa3dcd52919e75c6cdf6d5e
+  __DATA_CONST.__kalloc_var: 0x3c0 sha256:c653b623262a876b70be0df04d1abdf9b54779d7ec879878297ff93dc64700db
+  __DATA_CONST.__auth_got: 0x2c0 sha256:fe96278f7847c721ef6157e157760c2e92c352f928dc41dfcbd428a2c1feeb13
+  __DATA_CONST.__got: 0xb8 sha256:4cf95320f072b5627ec0af3a8a9cd114112d4c8a7325d890852c128822592529
+  UUID: 685EBBA3-C778-3DB3-A992-455DA21101AD
+  Functions: 844
   Symbols:   0
-  CStrings:  1497
+  CStrings:  1507
 
CStrings:
+ "%06ld.%06d %s::%s: device is target coalesced? %d\n"
+ "%06ld.%06d %s::%s: failed first port enable -- assume baseband is missing and populate baseband node with unknown values\n"
+ "%06ld.%06d %s::%s: invalid baseband device ID = %u, populating baseband with unknown values\n"
+ "%06ld.%06d %s::%s: set chipset unknown property? %d\n"
+ "%06ld.%06d %s::%s: setProperty success? RadioType: %d | ChipID: %d\n"
+ "%s: deviceID %x did not match any entry in static map; setting unknown properties\n\n"
+ "466"
+ "562"
+ "577"
+ "643"
+ "651"
+ "674"
+ "multi-cellular-platform"
+ "setUnknownProperties"
- "%06ld.%06d %s::%s: failed first port enable -- will assume baseband is missing\n"
- "%06ld.%06d %s::%s: invalid baseband device ID = %u\n"
- "454"
- "549"
- "564"
- "630"
- "638"
- "661"

```
