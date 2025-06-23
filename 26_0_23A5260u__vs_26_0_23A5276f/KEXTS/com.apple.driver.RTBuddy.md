## com.apple.driver.RTBuddy

> `com.apple.driver.RTBuddy`

```diff

-693.0.0.0.0
-  __TEXT.__cstring: 0x983d
+693.0.5.0.0
+  __TEXT.__cstring: 0x986f
   __TEXT.__os_log: 0x4e6
   __TEXT.__const: 0x2e0
-  __TEXT_EXEC.__text: 0x467f0
+  __TEXT_EXEC.__text: 0x468e4
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x128
   __DATA.__common: 0xb98

   __DATA_CONST.__got: 0x150
   __DATA_CONST.__mod_init_func: 0x148
   __DATA_CONST.__mod_term_func: 0x148
-  __DATA_CONST.__const: 0xb370
+  __DATA_CONST.__const: 0xb7b0
   __DATA_CONST.__kalloc_type: 0x1380
   __DATA_CONST.__kalloc_var: 0xf0
-  UUID: 84E8C8D3-D9F7-3D7E-99C4-04227ED0064F
-  Functions: 2338
+  UUID: FD20DB10-3A59-3080-9A59-6727E462F24B
+  Functions: 2337
   Symbols:   0
-  CStrings:  1083
+  CStrings:  1085
 
CStrings:
+ "%s coredump: iop is not active\n"
+ "121111121222121211111212121"
+ "12111122222222221111"
+ "121222111122"
+ "23:52:03"
+ "Jun 16 2025"
+ "_rtb->getWorkLoop()->inGate()"
+ "getEndpoint()->sendMessage(&msg) == kIOReturnSuccess"
+ "kIOReturnSuccess == _rtb->getWorkLoop()->runActionBlock(^IOReturn { switch (_state) { case TraceKitState::Unconfigured: return kIOReturnSuccess; case TraceKitState::Configured: case TraceKitState::Started: case TraceKitState::Stopped: break; } if (!_session->config.kdebug_managed) return kIOReturnSuccess; switch (reason) { case KD_CALLBACK_KDEBUG_ENABLED: case KD_CALLBACK_KDEBUG_DISABLED: return _enableGated(reason == KD_CALLBACK_KDEBUG_ENABLED); case KD_CALLBACK_SYNC_FLUSH: return _flushGated(); case KD_CALLBACK_TYPEFILTER_CHANGED: return kIOReturnSuccess; default: debug (ENDPOINT, \"Unimplemented kernel callback reason: %x\", reason); return kIOReturnSuccess; } })"
+ "nullptr != _epTraceKit"
- "!_processor->getWorkLoop()->onThread()"
- "121111222222222211"
- "12111211111121111211221111121212121"
- "12122211122"
- "19:19:32"
- "May 30 2025"
- "kIOReturnSuccess == _processor->getWorkLoop()->runActionBlock(^IOReturn { switch (_state) { case TraceKitState::Unconfigured: return kIOReturnSuccess; case TraceKitState::Configured: case TraceKitState::Started: case TraceKitState::Stopped: break; } if (!_session->config.kdebug_managed) return kIOReturnSuccess; switch (reason) { case KD_CALLBACK_KDEBUG_ENABLED: case KD_CALLBACK_KDEBUG_DISABLED: return _enableGated(reason == KD_CALLBACK_KDEBUG_ENABLED); case KD_CALLBACK_SYNC_FLUSH: return _flushGated(); case KD_CALLBACK_TYPEFILTER_CHANGED: return kIOReturnSuccess; default: debug (ENDPOINT, \"Unimplemented kernel callback reason: %x\", reason); return kIOReturnSuccess; } })"
- "sendMessage(&msg) == kIOReturnSuccess"

```
