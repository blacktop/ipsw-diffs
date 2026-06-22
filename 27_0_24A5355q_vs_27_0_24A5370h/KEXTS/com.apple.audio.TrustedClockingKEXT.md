## com.apple.audio.TrustedClockingKEXT

> `com.apple.audio.TrustedClockingKEXT`

```diff

-87.1.31.0.0
+92.30.0.0.0
   __TEXT.__const: 0x80 sha256:2de9c40b7576c599407d13cc930604faaf0df7cad2c576d65abf5a6ab2900625
-  __TEXT.__cstring: 0x2fe9 sha256:311c3297a5382fa60d9531e32a608ce91b80e74dab097b2112a969b49021f877
-  __TEXT_EXEC.__text: 0xb960 sha256:cf33adf9fb8112de1faeb45d6aba01a9802535951a8f0d50a0f5f917b3c77a4e
-  __TEXT_EXEC.__auth_stubs: 0x0
-  __DATA.__data: 0xc8 sha256:1e6c6448e94087dc27974a7cf59d3c2cb85b5001f25cf00e9869331313432b25
-  __DATA.__common: 0x88 sha256:b707241545a346265aab1ffb32ff64b55bf8f8dc1b56a46ef33ce3d15db11d33
+  __TEXT.__cstring: 0x31ae sha256:012541fe3d15b419013d559822979a6af46b6bbb699dfc348a4291ac40e5068a
+  __TEXT_EXEC.__text: 0xc2f4 sha256:c3ce883607523ec98041b2b751cb51766dc7efc07af5db5ea92d1389c1838278
+  __TEXT_EXEC.__auth_stubs: 0x500 sha256:e12c61486c41f01c9e26674a8d5d4955ddce97eaa4db6b487441c0cc8a6e0720
+  __DATA.__data: 0xc8 sha256:084022817e841289b04a6dc110c6cd44adb8dbe583933408b4362bcfbc553826
+  __DATA.__common: 0x60 sha256:2ea9ab9198d1638007400cd2c3bef1cc745b864b76011a0e1bc52180ac6452d4
   __DATA.__bss: 0x38 sha256:d4817aa5497628e7c77e6b606107042bbba3130888c5f47a375e6179be789fbb
-  __DATA_CONST.__mod_init_func: 0x18 sha256:a18767516b6e9787afd35a11d738ad2d86c4779e6d5860512c1f03520955c959
-  __DATA_CONST.__mod_term_func: 0x18 sha256:723eb630dba4c1cbf2007d4af28c9cd380542e2d2ad16cbda7b848d59ca16d89
-  __DATA_CONST.__const: 0x1728 sha256:8d12b8eb69839a95ba1e1d5ba233c85aa93faaa91c1f0793257e336081095c52
-  __DATA_CONST.__kalloc_type: 0xc0 sha256:b8be578c9442ca7af169a4d1c0fcc0804cfb63e469e7711f22fbe1710a53c9d8
-  __DATA_CONST.__auth_got: 0x298 sha256:cf97ae91397bd0e25595a0295da2c20ea2a047fdb87b8991c805b2def1a370eb
-  __DATA_CONST.__got: 0x50 sha256:1529dd68f95e5134d1505ecd77f2b008bec225188ac73522a80a02a9961a7d82
-  UUID: 098BDDEB-DD63-3003-80A0-106D2080FB8C
-  Functions: 435
+  __DATA_CONST.__mod_init_func: 0x10 sha256:c1a5b727373387f61a9a1257b06d971962d6b2cf64240b1c46ea35b384266d1d
+  __DATA_CONST.__mod_term_func: 0x10 sha256:53c2f54362376d939f0f31c25e49f9511fd82978f3aa77554cafd07de2a22608
+  __DATA_CONST.__const: 0x18d0 sha256:717b3be612c073fa4e182976bc7ed0d3217988e6d2f85b0c8cf791a72cfb402e
+  __DATA_CONST.__kalloc_type: 0x80 sha256:d8442f7267c3f9690b847e6f96af3c07e8c26edd1029d98187379f0fe3a23527
+  __DATA_CONST.__auth_got: 0x280 sha256:52e8899cf22cef0b654f779d9c7e4a7531a4241fe0e2b81d3ea406db4aaa4b7b
+  __DATA_CONST.__got: 0x40 sha256:df3d9bff377265f35dcde2529680b55c471a0db2e5c2e13fb08528175dc2507b
+  UUID: 0ADB88C1-A314-3DE8-A317-ECDD0526E057
+  Functions: 446
   Symbols:   0
-  CStrings:  154
+  CStrings:  139
 
CStrings:
+ "121111121222121211111111112211222112221122211222112221122211222112221122211222112221122211222112221122211211112111121121121111211211211211222222111112111121121121121111211211211211222222111112111121121121121111211211211211222222111112111121121121121111211211211211222222111112111121121121121111211211211211222222111112111121121121121111211211211211222222111112111121121121121111211211211211222222111112111121121121121111211211211211222222111112111121121121121111211211211211222222111112111121121121121111211211211211222222111112111121121121121111211211211211222222111112111121121121121111211211211211222222111112111121121121121111211211211211222222111112111121121121121111211211211211222222111112111121121121121111211211211211222222111112111121121121121111211211211211222222111112111121111122222222222222222222222222222222222222222222222222222222222222222121121211111"
+ "KernelCourierWorker::drain - sendMessage failed: %d for useCaseId %u\n"
+ "KernelCourierWorker::isUseCaseReady - Courier not initialized for useCaseId %u\n"
+ "KernelCourierWorker::isUseCaseReady - No state for useCaseId %u\n"
+ "KernelCourierWorker::sendTransactionToUseCase - ring full for useCaseId %u\n"
+ "TrustedClockingKEXT::start - Failed to start impl\n"
+ "TrustedClockingKEXTImpl::processKernelWorkloop [%u] - Exiting\n"
+ "TrustedClockingKEXTImpl::registerUseCaseState - add failed for useCaseId %u\n"
+ "TrustedClockingKEXTImpl::registerUseCaseState - registered useCaseId %u\n"
+ "TrustedClockingKEXTImpl::start - Failed to initialize courier worker\n"
+ "TrustedClockingKEXTImpl::startKernelWorkloop - No state for useCaseID %u\n"
+ "TrustedClockingKEXTImpl::startKernelWorkloop [%u] - PM notify failed\n"
+ "TrustedClockingKEXTImpl::startKernelWorkloop [%u] - failed to signal start\n"
+ "TrustedClockingKEXTImpl::stopKernelWorkloop - No state for useCaseID %u\n"
+ "TrustedClockingKEXTImpl::stopKernelWorkloop [%u] - PM notify failed\n"
+ "TrustedClockingKEXTImpl::stopKernelWorkloop [%u] - stop failed\n"
+ "TrustedClockingKEXTImpl::triggerWorkloopDataAvailability - No state for useCaseID %u\n"
+ "v16@?0^{TrustedClockingWorkloopContext={TightbeamServicesContainer=^^?{TightbeamModulusService=^^?B{coreaudiomodulus_coreaudiomodulusservice_s=^{tb_connection_s}}}{TightbeamDeviceService=^^?B{coreaudiodevice_coreaudiodevicetransportservice_s=^{tb_connection_s}}}{TightbeamCourierService=^^?B{coreaudiocourier_coreaudiocouriermessageservice_s=^{tb_connection_s}}}}{TrustedClockingKernelUtilities=^^?}{TrustedClockingSemaphore=^^?^{semaphore}B}{TrustedClockingSemaphore=^^?^{semaphore}B}{TrustedClockingSemaphore=^^?^{semaphore}B}{TrustedClockingSemaphore=^^?^{semaphore}B}{TrustedClockingMutex=^^?^{_IOLock}}{WorkloopSetup=QIQQQI}^{KernelSemaphore}^{KernelSemaphore}^{KernelSemaphore}^{KernelSemaphore}^{KernelMutex}ABABAB^{ServicesContainer}^{KernelUtilities}}8"
+ "v16@?0^{WorkloopContext={WorkloopSetup=QIQQQI}^{KernelSemaphore}^{KernelSemaphore}^{KernelSemaphore}^{KernelSemaphore}^{KernelMutex}ABABAB^{ServicesContainer}^{KernelUtilities}}8"
- "121111121222121211111222222222222222222222222222222222222222222222222222222222222222222121121111111111112222222222222222222222222222222222222222222222222"
- "12112112112112112112112111122222211111211"
- "TrustedClockingKEXT: sendTransactionToUseCase - ring full for use case %u\n"
- "TrustedClockingKEXT: sendTransactionToUseCase invalid for use case %u\n"
- "TrustedClockingKEXT::initCourierWorker - Failed to allocate queue lock\n"
- "TrustedClockingKEXT::initCourierWorker - Failed to allocate thread_call\n"
- "TrustedClockingKEXT::processCourierQueue - Courier not initialized for use case %u\n"
- "TrustedClockingKEXT::processCourierQueue - No state for use case %u\n"
- "TrustedClockingKEXT::processCourierQueue - messagearrived failed: %d for use case %u\n"
- "TrustedClockingKEXT::processKernelWorkloop [%u] - Exiting\n"
- "TrustedClockingKEXT::registerUseCaseState - Workloop state already registered for usecase %u\n"
- "TrustedClockingKEXT::registerUseCaseState - unable to create workloop state for use case ID %u\n"
- "TrustedClockingKEXT::setupKernelWorkloop - registered useCaseID %u\n"
- "TrustedClockingKEXT::start - Allocated workloop arrays \n"
- "TrustedClockingKEXT::start - Failed to allocate workloop states array\n"
- "TrustedClockingKEXT::start - Failed to initialize courier worker\n"
- "TrustedClockingKEXT::startKernelWorkloop - No registered state for useCaseID %u\n"
- "TrustedClockingKEXT::startKernelWorkloop [%u] - failed to notify PM state machine start\n"
- "TrustedClockingKEXT::startKernelWorkloop [%u] - failed to signal start\n"
- "TrustedClockingKEXT::startKernelWorkloop [%u] - start signal sent\n"
- "TrustedClockingKEXT::stop - All workloops exited\n"
- "TrustedClockingKEXT::stop - Released workloop states array\n"
- "TrustedClockingKEXT::stop - Signaling workloop %u to exit\n"
- "TrustedClockingKEXT::stop - WARNING: Errors waiting for workloops to exit\n"
- "TrustedClockingKEXT::stopKernelWorkloop - Error stopping workloop! %u\n"
- "TrustedClockingKEXT::stopKernelWorkloop - Signaled workloop to stop for useCaseID %u, waiting for exit...\n"
- "TrustedClockingKEXT::stopKernelWorkloop - State not found while stopping workloop! %u\n"
- "TrustedClockingKEXT::stopKernelWorkloop [%u] - failed to notify PM state machine stop\n"
- "TrustedClockingKEXT::triggerWorkloopDataAvailability - No state found for useCaseID %u\n"
- "WorkloopStateObject"
- "WorkloopStateObject::createWithSetup - failed to initialize workloop context\n"
- "WorkloopStateObject::createWithSetup - unable to initialize WorkloopStateObject\n"
- "WorkloopStateObject::init - unable to initialize OSObject\n"
- "site.WorkloopStateObject"

```
