## com.apple.driver.RTBuddy

> `com.apple.driver.RTBuddy`

```diff

-693.120.2.0.0
-  __TEXT.__cstring: 0x9a58 sha256:20a27b2b41f861d5daaa848818d507e47e5286d9fb4788abdc5fe3c554c93254
-  __TEXT.__os_log: 0x652 sha256:8f708edb1735a2004106434e5ba37495a9597650d01047e4d1ca6bd41910f599
-  __TEXT.__const: 0x280 sha256:0be9c1e6173e2eabc0836eb6742adb77565147cd16b32a228eff4c7f0099c4ed
-  __TEXT_EXEC.__text: 0x42078 sha256:a9af6773d35833fa6d63f67255124cc4f22196ef218035a1f2a041450464555d
+774.0.0.0.0
+  __TEXT.__cstring: 0x9d83 sha256:775514726e5b1540bde72116146539ef90c25cf4bf0f929104795719e50ea10e
+  __TEXT.__os_log: 0xba9 sha256:5c044c1e582a88c5a2bcf7ba7f154b539e3c6c48ffc363bb9d9f51c43997d3b3
+  __TEXT.__const: 0x2a8 sha256:df5073bc081a76c9ba72839d73daf3e145880f127c6b2a504434f5ebb00e42aa
+  __TEXT_EXEC.__text: 0x449c0 sha256:4cfa0bdd7fa9c6d2e3da270cf4b1bddda21487268b856c343bdc2ab50e603692
   __TEXT_EXEC.__auth_stubs: 0x0
-  __DATA.__data: 0x128 sha256:ca1c39bdf19daa06085fbc95491d2f78436f1086e4ada79958e3cff87bb29a71
-  __DATA.__common: 0xbc0 sha256:f6f2312cfd2cfb62ea672e8de4c0ceca1c8de3ba3d8fcd02e8e5840d26d97574
-  __DATA_CONST.__auth_got: 0x548 sha256:105871677fc48765e7b0acb1e20c16858d7a49df2c8df930d1ceb7c349f82bc8
-  __DATA_CONST.__got: 0x158 sha256:313f778fc515e6299823ffe1719f5933c814d695f12ecb0b067610ea221ef747
-  __DATA_CONST.__mod_init_func: 0x150 sha256:4cededa940f55faae9fafa54e69a196471d3376aac82786edaf8c68c4942af0a
-  __DATA_CONST.__mod_term_func: 0x150 sha256:297982b20cbf3040fb9792b0a2ad11928f31ce98cda1aee66c1ce17d8126f869
-  __DATA_CONST.__const: 0xbf58 sha256:5b2eb8f437331d7795bf04494cd339025a707c5b639ca81702d1ad87479b5148
-  __DATA_CONST.__kalloc_type: 0x13c0 sha256:51bf1265fd95356184a94d4a78c13238d1f1424eaaf4487a2d7ffcad7ad40f49
-  __DATA_CONST.__kalloc_var: 0xf0 sha256:2a153e3d6f6e35cf5c2c534f2b545fbebc5eb9a5313469c7799c1fdcb8df2679
-  UUID: 5D9FC402-C010-35A1-8D1A-5E78B44EB0B7
+  __DATA.__data: 0x128 sha256:3eee8bdcb293f304b28f26fc23c5111fdaaeafdbf0e3fdc2329cf9c90f0e97ae
+  __DATA.__common: 0xb70 sha256:e96664fb07aec667ccc49803398759e66f4ec2f4ac6511ec2ea0dd35b350a16c
+  __DATA_CONST.__mod_init_func: 0x140 sha256:baa6b84413ae54089529e0bafb23241b4d4768d9e928311cc17b47de262055b8
+  __DATA_CONST.__mod_term_func: 0x140 sha256:b6cfbf63406f59783b7ff028d8324236da74755f76c75bc37d90d2b8ec3c20da
+  __DATA_CONST.__const: 0xbce8 sha256:1a830eeffbbc65a8bfa5343a3bc31f328d0295133b5be7484ce1cafb89184974
+  __DATA_CONST.__kalloc_type: 0x1340 sha256:ee8d7a10e3fc71c6ffef36055bfc4c2f6bf3d0b6be74bb51b5d721d190108f27
+  __DATA_CONST.__kalloc_var: 0xf0 sha256:db8fa355e0bf6d6443c884e31c45f912a8111dbe1aa15439183641a0b306a442
+  __DATA_CONST.__auth_got: 0x590 sha256:4ea104b36dbb36d43e3a914389dd40102a719b3eb4bb7bd6e817869034a67e1f
+  __DATA_CONST.__got: 0x168 sha256:62cba548337cceeabaa8f92501874c8464ea42a95c1ab0769a5c079ebff6b4bd
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
