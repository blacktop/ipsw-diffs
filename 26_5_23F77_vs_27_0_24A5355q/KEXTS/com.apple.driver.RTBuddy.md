## com.apple.driver.RTBuddy

> `com.apple.driver.RTBuddy`

```diff

-693.120.2.0.0
-  __TEXT.__cstring: 0x9a58
-  __TEXT.__os_log: 0x652
-  __TEXT.__const: 0x280
-  __TEXT_EXEC.__text: 0x42078
+774.0.0.0.0
+  __TEXT.__cstring: 0x9d83
+  __TEXT.__os_log: 0xba9
+  __TEXT.__const: 0x2a8
+  __TEXT_EXEC.__text: 0x449c0
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x128
-  __DATA.__common: 0xbc0
-  __DATA_CONST.__auth_got: 0x548
-  __DATA_CONST.__got: 0x158
-  __DATA_CONST.__mod_init_func: 0x150
-  __DATA_CONST.__mod_term_func: 0x150
-  __DATA_CONST.__const: 0xbf58
-  __DATA_CONST.__kalloc_type: 0x13c0
+  __DATA.__common: 0xb70
+  __DATA_CONST.__mod_init_func: 0x140
+  __DATA_CONST.__mod_term_func: 0x140
+  __DATA_CONST.__const: 0xbce8
+  __DATA_CONST.__kalloc_type: 0x1340
   __DATA_CONST.__kalloc_var: 0xf0
-  UUID: 5D9FC402-C010-35A1-8D1A-5E78B44EB0B7
+  __DATA_CONST.__auth_got: 0x590
+  __DATA_CONST.__got: 0x168
+  UUID: D221D7D1-E6FD-3B9B-9CFD-DCF4A6F20C4B
   Functions: 2406
   Symbols:   0
-  CStrings:  1097
+  CStrings:  1127
 
CStrings:
+ "!_rtb->hibernateReuseMappings() || _bufferMemoryDescriptor == nullptr || _bufferMemoryDescriptor->getLength() >= _bufferSize"
+ "!_validDimensions || (_processor->hibernateReuseMappings() && _maxEntries == syslog_get_max_entries(msg) && _maxMessageSize == syslog_get_max_message_size(msg))"
+ "!rtb->hibernateReuseMappings() || _bufferMemoryDescriptor == nullptr || _bufferMemoryDescriptor->getLength() >= _bufferSize"
+ "\"Assertion failed: \" \"_layoutBuffer\" @%s:%d"
+ "\"Assertion failed: \" \"_layoutLock.has_value()\" @%s:%d"
+ "\"RTBuddy(%s)::%s \" \"%s:%u: REQUIRE failed: %s, \" \"IOP provided invalid segment for coredump (base 0x%llx, size 0x%lx)\" @%s:%d"
+ "\"RTBuddy(%s)::%s \" \"%s:%u: REQUIRE failed: %s, %s\" @%s:%d"
+ "(!_rtb->hibernateReuseMappings() || cmdType == CRASHLOG_BUFFER)"
+ "121111121222121211121111222111112221222222121222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222221111121111111111111121212222221111"
+ "12221122"
+ "1222121121"
+ "1222121121121"
+ "1222121122211"
+ "22:52:24"
+ "IOVirtualAddress RTBuddyCoredumpMap::physToVirt(IOPhysicalAddress, IOByteCount)"
+ "May 27 2026"
+ "RTBuddy(%s): Error processing metric in log entry"
+ "RTBuddy(%s): Failed to append string table chunk"
+ "RTBuddy(%s): Failed to create string table"
+ "RTBuddy(%s): Registering log role for %s/%s"
+ "RTBuddy(%s): String table info not found for source_info"
+ "RTBuddy(%s): Unable to reserve layout space: %llu bytes"
+ "RTBuddy(%s): configure hw_trace %u"
+ "RTBuddy(%s): configure sw_trace %u"
+ "RTBuddy(%s): decode buffer too small: %zu < %zu bytes"
+ "RTBuddy(%s): image_layout_t did not match current space: (%u, %u)"
+ "RTBuddy(%s): image_layout_t was not sequential: (%u, %u)"
+ "RTBuddy(%s): invalidate layout"
+ "RTBuddy(%s): log entry size too small: %zu < %zu bytes"
+ "RTBuddy(%s): received image layout for space %u image %u"
+ "RTBuddy(%s): received space layout for space %u with %u images"
+ "RTBuddy(%s): received system layout with %u address spaces"
+ "RTBuddy(%s): space_layout_t was not sequential: (%u, %u)"
+ "RTBuddy(%s): system_layout_t was not received"
+ "RTBuddy(%s): tracekit message too small: %zu < %llu bytes"
+ "RTBuddy(%s): tracekit version mismatch: msg=%u expected=%u type=%u"
+ "RTBuddyBinaryLogEntryHandlerMetric"
+ "Section size error.  Crashlog section header (%zu bytes) larger than remaining buffer (%llu bytes)"
+ "Section size error.  Signature %#0x, version %#0x, section (%u bytes) larger than remaining buffer (%llu bytes)"
+ "_bufferMemoryDescriptor->getRetainCount() == 1"
+ "_builtinEntryHandlers[kMetricHandlerIndex]"
+ "_builtinEntryHandlers[kOSLogHandlerIndex]"
+ "_builtinEntryHandlers[kSysLogHandlerIndex]"
+ "_builtinEntryHandlers[kTraceKitHandlerIndex]"
+ "_kdebugMemoryDecriptor->getRetainCount() == 1"
+ "expected buffer to be release-able"
+ "hibernate-reuse-mappings"
+ "hist != nullptr"
+ "obj != nullptr"
+ "oldBufferSize >= _bufferSize"
+ "physToVirt"
+ "site.RTBuddyBinaryLogEntryHandlerMetric"
- "!_validDimensions"
- "1211111111111111112"
- "1211111212221212111211112221111122212222221212222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222211111211111111111111212122222211112"
- "1222112"
- "1222121"
- "1222122"
- "20:30:46"
- "Apr 23 2026"
- "RTBuddyTraceChunkEncoder"
- "RTBuddyTraceDataEncoder"
- "RTBuddyTraceKitMessageEncoder"
- "Section size error.  Crashlog section header (%zu bytes) larger than remaining buffer (%zu bytes)"
- "Section size error.  Signature %#0x, version %#0x, section (%u bytes) larger than remaining buffer (%zu bytes)"
- "_builtinEntryHandlers[BUILTIN_IDX(LOG_TYPE_OS_LOG)]"
- "_builtinEntryHandlers[BUILTIN_IDX(LOG_TYPE_SYSLOG)]"
- "_builtinEntryHandlers[BUILTIN_IDX(LOG_TYPE_TRACEKIT)]"
- "_builtinEntryHandlers[BUILTIN_IDX(type)]"
- "handleEntry"
- "site.RTBuddyTraceChunkEncoder"
- "site.RTBuddyTraceDataEncoder"
- "site.RTBuddyTraceKitMessageEncoder"
- "void RTBuddyBinaryLogHandler::handleEntry(uint8_t, OSBoundedPtr<log_entry>, struct logSourceInfo *)"

```
