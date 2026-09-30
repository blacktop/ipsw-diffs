## com.apple.driver.RTBuddy

> `com.apple.driver.RTBuddy`

```diff

-618.100.37.0.0
-  __TEXT.__cstring: 0x90c6
-  __TEXT.__os_log: 0x4fb
-  __TEXT.__const: 0x2e8
-  __TEXT_EXEC.__text: 0x422a0
+693.0.0.0.0
+  __TEXT.__cstring: 0x983d
+  __TEXT.__os_log: 0x4e6
+  __TEXT.__const: 0x2e0
+  __TEXT_EXEC.__text: 0x467f0
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x128
-  __DATA.__common: 0xb48
-  __DATA_CONST.__auth_got: 0x500
-  __DATA_CONST.__got: 0x148
-  __DATA_CONST.__mod_init_func: 0x140
-  __DATA_CONST.__mod_term_func: 0x140
-  __DATA_CONST.__const: 0xa8b0
-  __DATA_CONST.__kalloc_type: 0x1300
+  __DATA.__common: 0xb98
+  __DATA_CONST.__auth_got: 0x540
+  __DATA_CONST.__got: 0x150
+  __DATA_CONST.__mod_init_func: 0x148
+  __DATA_CONST.__mod_term_func: 0x148
+  __DATA_CONST.__const: 0xb370
+  __DATA_CONST.__kalloc_type: 0x1380
   __DATA_CONST.__kalloc_var: 0xf0
-  UUID: D48C6773-51B5-3DB4-900C-318B1E4CB837
-  Functions: 2214
+  UUID: 84E8C8D3-D9F7-3D7E-99C4-04227ED0064F
+  Functions: 2338
   Symbols:   0
-  CStrings:  1044
+  CStrings:  1083
 
CStrings:
+ "\"Assertion failed: \" \"buffer.size_bytes() >= entry.key_len + data_len\" @%s:%d"
+ "\"RTBuddy(%s)::%s \" \"Entropy: invalid message 0x%016llx received (cmd=0x%x)\" \"\\n%s\" @%s:%d"
+ "1211111212221212111111111111212211"
+ "12111112122212121111121"
+ "12111211111121111211221111121212121"
+ "12122211122"
+ "19:19:32"
+ "B20@?0i8Q12"
+ "Entropy (count: %zu) requested"
+ "IOReturn RTBuddyTraceKitEndpoint::_configureGated(rtbuddy_trace_config_t, OSSharedPtr<RTBuddyTraceKitSession> &)"
+ "IOReturn RTBuddyTraceKitEndpoint::_configureGated(rtbuddy_trace_config_t, OSSharedPtr<RTBuddyTraceKitSession> &)_block_invoke"
+ "IOReturn RTBuddyTraceKitEndpoint::_enableGated(const bool)"
+ "IOReturn RTBuddyTraceKitEndpoint::_flushGated()"
+ "IOReturn RTBuddyTraceKitEndpoint::_hostVersionGated()"
+ "IOReturn RTBuddyTraceKitEndpoint::_powerStateCallbackGated(const unsigned long *, const unsigned long *)"
+ "IOReturn RTBuddyTraceKitEndpoint::_resetGated()"
+ "IOReturn RTBuddyTraceKitEndpoint::_unconfigureGated()"
+ "IOReturn RTBuddyTraceKitEndpoint::attach(rtbuddy_trace_attach_t, OSSharedPtr<RTBuddyTraceKitSession> &)_block_invoke"
+ "IOReturn RTBuddyTraceKitEndpoint::releaseChunkCPUTrace(rtbuddy_cputrace_chunk_t)_block_invoke"
+ "May 30 2025"
+ "RTBuddy(%s)::%s: Initial configuration failed with status 0x%x\n"
+ "RTBuddyEntropyEndpoint"
+ "RTBuddyEntropyEndpoint.cpp"
+ "RTBuddyTraceKitSession"
+ "RTBuddyUserClient::clientMemoryForType (0x%x)\n"
+ "RTBuddyUserClient::registerNotificationPort (0x%x)\n"
+ "_buffer->enableNoAllocLocalCopy() == kIOReturnSuccess"
+ "_configureGated"
+ "_configureGated_block_invoke"
+ "_enableGated"
+ "_endpointActive"
+ "_flushGated"
+ "_handleEntropyRequest"
+ "_hostVersionGated"
+ "_initializationThread"
+ "_powerStateCallbackGated"
+ "_resetGated"
+ "_resetGated() == kIOReturnSuccess"
+ "_session"
+ "_session == nullptr"
+ "_setEndpointActiveGated"
+ "_state == TraceKitState::Unconfigured"
+ "_state == _stateIOP"
+ "_stateIOP == TraceKitState::Configured"
+ "_unconfigureGated"
+ "_waitForBusyACKGated"
+ "_waitForEndpointActiveGated"
+ "_waitForStateTransitionsGated"
+ "attach_block_invoke"
+ "default_role.size() + _roleSize + (_roleSize ? 1 : 0) + 1 <= sizeof(source_info->role)"
+ "entropy"
+ "entropy_msg_cmd(msg) == ENTROPY_MSG_ENTROPY_GENERATE"
+ "i8@?0"
+ "kIOReturnSuccess == _processor->getWorkLoop()->runActionBlock(^IOReturn { switch (_state) { case TraceKitState::Unconfigured: return kIOReturnSuccess; case TraceKitState::Configured: case TraceKitState::Started: case TraceKitState::Stopped: break; } if (!_session->config.kdebug_managed) return kIOReturnSuccess; switch (reason) { case KD_CALLBACK_KDEBUG_ENABLED: case KD_CALLBACK_KDEBUG_DISABLED: return _enableGated(reason == KD_CALLBACK_KDEBUG_ENABLED); case KD_CALLBACK_SYNC_FLUSH: return _flushGated(); case KD_CALLBACK_TYPEFILTER_CHANGED: return kIOReturnSuccess; default: debug (ENDPOINT, \"Unimplemented kernel callback reason: %x\", reason); return kIOReturnSuccess; } })"
+ "names.empty()"
+ "nullptr != entropy"
+ "releaseChunkCPUTrace_block_invoke"
+ "reset() == kIOReturnSuccess"
+ "rtb_cputrace_carveout_mb"
+ "sendMessage(&msg) == kIOReturnSuccess"
+ "site.RTBuddyEntropyEndpoint"
+ "site.RTBuddyTraceKitSession"
+ "size_needed <= caSpan.size()"
+ "uuids.empty()"
+ "void RTBuddyEntropyEndpoint::_handleEntropyRequest(mbi_msg_t)"
+ "void RTBuddyTraceKitEndpoint::_setEndpointActiveGated(bool)"
+ "void RTBuddyTraceKitEndpoint::_waitForBusyACKGated(void *)"
+ "void RTBuddyTraceKitEndpoint::_waitForEndpointActiveGated()"
+ "void RTBuddyTraceKitEndpoint::_waitForStateTransitionsGated()"
- "\"Assertion failed: \" \"buffer_len >= entry.key_len + data_len\" @%s:%d"
- "\"Assertion failed: \" \"buffer_len >= sizeof(entry)\" @%s:%d"
- "121111121222121211111111111121221"
- "121112111111211112112211111212221"
- "20:30:47"
- "Apr 22 2025"
- "IOReturn RTBuddyTraceKitEndpoint::_tracekitSendEnabledState(const bool *)"
- "IOReturn RTBuddyTraceKitEndpoint::_tracekitSendFlushRequest()"
- "IOReturn RTBuddyTraceKitEndpoint::_tracekitSendHostReady()"
- "OSString *RTBuddy::_segmentTokenizer(char *, char *, char **, const char) const"
- "RTBuddy(%s)::%s: Failed to send enabled state packet - 0x%x\n"
- "RTBuddy(%s)::%s: Failed to send flush request - 0x%x\n"
- "TraceKit endpoint: Notifying IOP that tracing is %s"
- "_segmentTokenizer"
- "_tracekitSendEnabledState"
- "_tracekitSendFlushRequest"
- "_tracekitSendHostReady"
- "begin"
- "disabled"
- "enabled"
- "event"
- "iter < end"
- "iterator == nullptr"
- "kIOReturnSuccess == _processor->getWorkLoop()->runAction (OSMemberFunctionCast (IOWorkLoop::Action, this, &RTBuddyTraceKitEndpoint::_tracekitSendFlushRequest), this)"
- "kIOReturnSuccess == _processor->getWorkLoop()->runAction (OSMemberFunctionCast(IOWorkLoop::Action, this, &RTBuddyTraceKitEndpoint::_tracekitSendEnabledState), this, &new_state)"
- "kIOReturnSuccess == _processor->getWorkLoop()->runAction (OSMemberFunctionCast(IOWorkLoop::Action, this, &RTBuddyTraceKitEndpoint::_tracekitSendHostReady), this)"
- "name != nullptr"
- "size_needed <= caData->getLength()"
- "slice_uuid != nullptr"
- "virtual void RTBuddyTraceKitEndpoint::enable()"

```
