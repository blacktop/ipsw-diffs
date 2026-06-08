## com.apple.driver.corecapture

> `com.apple.driver.corecapture`

```diff

-1330.5.0.0.0
-  __TEXT.__os_log: 0x4336
+1355.39.0.0.0
+  __TEXT.__os_log: 0x4680
   __TEXT.__const: 0x110
-  __TEXT.__cstring: 0x200e
-  __TEXT_EXEC.__text: 0x2614c
+  __TEXT.__cstring: 0x2082
+  __TEXT_EXEC.__text: 0x27c84
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc4
   __DATA.__common: 0x308
   __DATA.__bss: 0x2ac
-  __DATA_CONST.__auth_got: 0x3a8
-  __DATA_CONST.__got: 0xd0
   __DATA_CONST.__mod_init_func: 0x88
   __DATA_CONST.__mod_term_func: 0x80
   __DATA_CONST.__const: 0x7010
   __DATA_CONST.__kalloc_type: 0x10c0
   __DATA_CONST.__kalloc_var: 0xa0
-  UUID: 0E29FEFB-34F6-39D4-9367-AD4E5A81CEA4
-  Functions: 878
+  __DATA_CONST.__auth_got: 0x3a8
+  __DATA_CONST.__got: 0xd8
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
