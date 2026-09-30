## com.apple.driver.corecapture

> `com.apple.driver.corecapture`

```diff

-1330.5.0.0.0
-  __TEXT.__os_log: 0x4336 sha256:40d098abfb866e0e24a5cee480bf25adbf9d679b041e4d4dcb4d74aa89c8e3f4
+1355.39.0.0.0
+  __TEXT.__os_log: 0x4680 sha256:7441837148f55b9b3669a154ed1f32113c91fbc24bf1106b896f8e2f8f2b79ea
   __TEXT.__const: 0x110 sha256:c2385c75333b3266e531be9252db0cef3fd540e7d0108c8abbb988a529246296
-  __TEXT.__cstring: 0x200e sha256:7bd92076663884ff4693f131761f76eb8989512a4d8f753beb1cfce930b865eb
-  __TEXT_EXEC.__text: 0x2614c sha256:27dc3ace7c94275d0e26e78f7098d87dcdc9ce359a54546c5d1f33af84517b8d
+  __TEXT.__cstring: 0x2082 sha256:48f30c9f2ae47d5dc4bb6c841ad6e211076fa7045912771547f0216c824448f0
+  __TEXT_EXEC.__text: 0x27c84 sha256:da1437668546a2136596c87736515baf9de2dda5a81a74b119a815b0ae9054da
   __TEXT_EXEC.__auth_stubs: 0x0
-  __DATA.__data: 0xc4 sha256:75606948140b0b79e67c487655d47a42d5b0d302b6dbab5688355f63d77124ae
+  __DATA.__data: 0xc4 sha256:c016a8685a8109443f5edb1621b609d3c93e111cd8462a1807732d5f56232bfa
   __DATA.__common: 0x308 sha256:508f5ba745944e982367cdbcd6a240acc7f895583df43b519b7d6745f5d86f7b
   __DATA.__bss: 0x2ac sha256:101bb8aeab946925b14006ee79fbfa56dcf5b2a65c44ca9b435abbd1abe3a22b
-  __DATA_CONST.__auth_got: 0x3a8 sha256:84b7d6688956fd0ac90006aabf3c19726983dd2d86e164c20e0ac2fbf4aa3816
-  __DATA_CONST.__got: 0xd0 sha256:13f9535a4e01fccfdc03dc5e16b2333d05fe736b5c93f818e6f179578ab3e800
-  __DATA_CONST.__mod_init_func: 0x88 sha256:78f7ecba5a76399843f9d9d603b2a6d385aa7165825fe66002c134fe439aec36
-  __DATA_CONST.__mod_term_func: 0x80 sha256:fe59a52b20517015cd92bc6d03a5b396d94e528e5b7efc6cfb6883aa5a450f69
-  __DATA_CONST.__const: 0x7010 sha256:316102e0b41b9daa4490b184ad1e5eb57758c3df11549dc3ed8fd244b33d3370
-  __DATA_CONST.__kalloc_type: 0x10c0 sha256:80164214436bba3ec4ce8ab2489c574407e9d44fbfd24f790f17bdd037f86986
-  __DATA_CONST.__kalloc_var: 0xa0 sha256:bb4d5d195c28c90b1d1ffce6962f9f454175caaf73b95e8002242aff9befb1c2
-  UUID: 0E29FEFB-34F6-39D4-9367-AD4E5A81CEA4
-  Functions: 878
+  __DATA_CONST.__mod_init_func: 0x88 sha256:251acbac7e3f0002c7ddc83c937a967462cf43f72fb5b403c3f55ee72e2a23e8
+  __DATA_CONST.__mod_term_func: 0x80 sha256:9d22fa00ca7a5204b0f2895b26c559a0be917e5bd96d240ad190127f2fd26eee
+  __DATA_CONST.__const: 0x7010 sha256:6ef168c0b8a03f4e8398cade8dc60dfa71cc1349ddf80aa40bc81440caed5e0b
+  __DATA_CONST.__kalloc_type: 0x10c0 sha256:e9c6e5af105636ea5f0f3827b63c8109912b1c61882a1c2d5452febe79a417e2
+  __DATA_CONST.__kalloc_var: 0xa0 sha256:9c932a13d6d9e2ae9ef496d6bbb7cbbe96420102ea1cb7aa82b406ee9e7336f4
+  __DATA_CONST.__auth_got: 0x3a8 sha256:12013ae4ef80d93f53d0cfe375aa4ea5308b1b1db105ae40c23d7f2d63f9d666
+  __DATA_CONST.__got: 0xd8 sha256:d42106bd7217933a3b4029a3c5702efad3e235b191f4ca10c8e5d3f519aa9f85
+  UUID: 7341D4D1-2BC1-306C-A8DA-AFFDA403287A
+  Functions: 880
   Symbols:   0
-  CStrings:  661
+  CStrings:  673
 
CStrings:
+ "%s::%s() Failed to set property dictionary Owner:%s Pipe:%s\n"
+ "%s::%s(): Invalid log data type - %d Owner:%s Pipe:%s\n"
+ "%s::%s(): Invalid log policy - %d Owner:%s Pipe:%s\n"
+ "%s::%s(): Invalid log type - %d Owner:%s Pipe:%s\n"
+ "%s::%s(): Min Log Size To Notify(%zd) is greater than Log Size(%zd) Owner:%s Pipe:%s\n"
+ "%s::%s(): Terminating CCCapture object\n"
+ "%s::%s(): initWithOwnerNameCapacity failed Owner:%s Pipe:%s\n"
+ "%s::%s():Failed to set Min Log Size To Notify property (%zd) Owner:%s Pipe:%s\n"
+ "%s::%s():Failed to set notify timeout property (%u) Owner:%s Pipe:%s\n"
+ "%s::%s():Failed to set pipe Log type property (%d) Owner:%s Pipe:%s\n"
+ "%s::%s():Failed to set pipe compression property (%d) Owner:%s Pipe:%s\n"
+ "%s::%s():Failed to set pipe data type property (%d) Owner:%s Pipe:%s\n"
+ "%s::%s():Failed to set pipe directory name property (%s) Owner:%s Pipe:%s\n"
+ "%s::%s():Failed to set pipe file name property (%s) Owner:%s Pipe:%s\n"
+ "%s::%s():Failed to set pipe file option flags property (%u) Owner:%s Pipe:%s\n"
+ "%s::%s():Failed to set pipe log identifier property (%s) Owner:%s Pipe:%s\n"
+ "%s::%s():Failed to set pipe name property (%s) Owner:%s Pipe:%s\n"
+ "%s::%s():Failed to set pipe owner property (%s) Owner:%s Pipe:%s\n"
+ "%s::%s():Failed to set pipe policy property (%d) Owner:%s Pipe:%s\n"
+ "%s::%s():Failed to set pipe size property (%zd) Owner:%s Pipe:%s\n"
+ "%s::%s():Failed to set pipe type property (%d) Owner:%s Pipe:%s\n"
+ "%s::%s():Failed to set total file number property (%u) Owner:%s Pipe:%s\n"
+ "%s::%s():Failed to set total file size property (%u) Owner:%s Pipe:%s\n"
+ "%s::%s():Failed to set unified log policy property (%d) Owner:%s Pipe:%s\n"
+ "%s::%s:%d Name: %s LogIdentifier: %s"
+ "%s::%s:%d Owner: %s Name: %s LogIdentifier: %s"
+ "111122222221112212222222221121"
+ "112211212222"
+ "22222222222222222222222222222222222222111"
+ "CCDataPipe::enqueueBlob queue full, dropping blob: %s session: %s Owner: %s Name: %s queueSize: %zu maxSize: %zu"
+ "CCDataPipe::stop Owner: %s Name: %s enqueued: %llu dequeued: %llu dropped: %llu"
+ "CCFaultReporter: Failed to create properties dictionary\n"
+ "CCFaultReporter: Failed to create service name string\n"
+ "CCFaultReporterService"
+ "CCLogPipe::notifyUserSpace capture notification dropped - no user client for owner: %s pipe: %s\n"
+ "CCPipe::initWithOwnerNameCapacity failed Owner:%s Pipe:%s\n"
+ "CoreCapture errorCodeStr for last fault reason code %d : \n"
+ "CoreCapture errorCodeStr for last fault status code %d : \n"
+ "Failed opening CCLogPipeUserClient Owner:%s Pipe:%s\n"
+ "Failed to create lock Owner:%s Pipe:%s\n"
+ "Failed to create ring MD Owner:%s Pipe:%s\n"
+ "Failed to create ring buffer Owner:%s Pipe:%s\n"
+ "Failed to create ring state Owner:%s Pipe:%s\n"
+ "Failed to create scratch bufferes Owner:%s Pipe:%s\n"
+ "IOLockAlloc failed Owner:%s Pipe:%s\n"
+ "IOMallocType failed Owner:%s Pipe:%s\n"
+ "Triggering faultReport with reason '%s'\n"
+ "Unknown"
+ "missing pipeOptions Owner:%s Pipe:%s\n"
+ "unknown"
- "%s:%d Pipe Owner:%s Name:%s LogIdentifier:%s"
- "%s:%d stream Name:%s LogIdentifier:%s"
- "%s::%s() Failed to set property dictionary \n"
- "%s::%s(): Attempt to acquire fCCCaptureLock\n"
- "%s::%s(): Invalid log data type - %d\n"
- "%s::%s(): Invalid log type - %d\n"
- "%s::%s(): Release fCCCaptureLock\n"
- "%s::%s(): Terminate and Clear CCCapture object, terminate it first\n"
- "%s::%s(): initWithOwnerNameCapacity failed\n"
- "%s::%s():Failed to set Min Log Size To Notify property (%zd) \n"
- "%s::%s():Failed to set notify timeout property (%u) \n"
- "%s::%s():Failed to set pipe Log type property (%d) \n"
- "%s::%s():Failed to set pipe compression property (%d) \n"
- "%s::%s():Failed to set pipe directory name property (%s) \n"
- "%s::%s():Failed to set pipe file name property (%s) \n"
- "%s::%s():Failed to set pipe file option flags property (%u) \n"
- "%s::%s():Failed to set pipe log identifier property (%s) \n"
- "%s::%s():Failed to set pipe name property (%s) \n"
- "%s::%s():Failed to set pipe owner property (%s) \n"
- "%s::%s():Failed to set pipe policy property (%d) \n"
- "%s::%s():Failed to set pipe size property (%zd) \n"
- "%s::%s():Failed to set pipe type property (%d) \n"
- "%s::%s():Failed to set total file number property (%u) \n"
- "%s::%s():Failed to set total file size property (%u) \n"
- "%s::%s():Failed to set unified log policy property (%d) \n"
- "11122222221112212222222221121"
- "112211212"
- "22222222111"
- "CCPipe::initWithOwnerNameCapacity failed\n"
- "CoreCapture errorCodeStr for fault %s \n"
- "CoreCapture errorCodeStr for fault status Code %d : \n"
- "Failed Opening CCLogPipeUserClient\n"
- "Failed to create lock\n"
- "Failed to create ring MD\n"
- "Failed to create ring buffer\n"
- "Failed to create ring state\n"
- "Failed to create scratch bufferes\n"
- "setCCaptureInRegistry"

```
