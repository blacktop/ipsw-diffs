## xhc.t6050.im4p

> `Firmware/xhc.t6050.im4p`

### Sections with Same Size but Changed Content

- `__TEXT._rtk_vtor`
- `__TEXT._rtk_mtab`
- `__TEXT.__rebase_info`
- `__DATA.__const`
- `__DATA.__data`
- `__DATA._rtk_patchbay`
- `__DATA.__nl_symbol_ptr`
- `__OS_LOG.__string`
- `__VTOR._rtk_vtor_patch`

```diff

-  __TEXT.__text: 0x15d88
+  __TEXT.__text: 0x15e5c
   __TEXT._rtk_vtor: 0x300
-  __TEXT.__const: 0x7d4
+  __TEXT.__const: 0x7e4
   __TEXT._rtk_mtab: 0x194
   __TEXT.__cstring: 0x1a5f
   __TEXT.__constructor: 0x0
CStrings:
+ "endpoint.c:348::@XHCAddrTag(%08x) Wait EP for no outstandings"
+ "endpoint.c:357::@XHCAddrTag(%08x) Wait EP for no flow control"
+ "endpoint.c:361::@XHCAddrTag(%08x) Wait EP for no DB outstandings failed due to @Enum(RTK_status(%u))"
+ "endpoint.c:409::@XHCAddrTag(%08x) stop endpoint request aborted"
+ "endpoint.c:439::Endpoint Update Stream Context: Invalid stream ID - internal_endpoint_id=%u, latest_stream_id=%u, #streams=%u"
+ "endpoint.c:551::@XHCAddrTag(%08x) Endpoint Stop Barrier Handler"
+ "endpoint.c:620::@XHCAddrTag(%08x) Endpoint Pre Stop Request"
+ "endpoint.c:678::@XHCAddrTag(%08x) Endpoint Post Stop Request, Status = @Enum(RTK_status(%u))"
+ "endpoint.c:727::@XHCAddrTag(%08x) Endpoint Stop Request"
+ "endpoint.c:730::@XHCAddrTag(%08x) Skip Endpoint Stop Request, Pre Stop Status = @Enum(RTK_status(%u))"
+ "endpoint.c:759::@XHCAddrTag(%08x) Endpoint Set TR DQPTR: Invalid stream ID, latest_stream_id=%u, #streams=%u"
+ "endpoint.c:776::@XHCAddrTag(%08x) DB Ring to stopped EP"
+ "endpoint.c:804::@XHCAddrTag(%08x) Flush Stop EP, completion_code=@Enum(trb_completion_code_t(%u))"
+ "endpoint.c:817::@XHCAddrTag(%08x) Warning! endpoint_flush_stop_ep_event_handler received unexpected stop endpoint completion event"
+ "main.c:32::XHC firmware started (FW build version: AppleXHCFirmware-242.40.2~138.t6050)"
- "endpoint.c:331::@XHCAddrTag(%08x) Wait EP for no outstandings"
- "endpoint.c:340::@XHCAddrTag(%08x) Wait EP for no flow control"
- "endpoint.c:344::@XHCAddrTag(%08x) Wait EP for no DB outstandings failed due to @Enum(RTK_status(%u))"
- "endpoint.c:392::@XHCAddrTag(%08x) stop endpoint request aborted"
- "endpoint.c:422::Endpoint Update Stream Context: Invalid stream ID - internal_endpoint_id=%u, latest_stream_id=%u, #streams=%u"
- "endpoint.c:534::@XHCAddrTag(%08x) Endpoint Stop Barrier Handler"
- "endpoint.c:603::@XHCAddrTag(%08x) Endpoint Pre Stop Request"
- "endpoint.c:661::@XHCAddrTag(%08x) Endpoint Post Stop Request, Status = @Enum(RTK_status(%u))"
- "endpoint.c:710::@XHCAddrTag(%08x) Endpoint Stop Request"
- "endpoint.c:713::@XHCAddrTag(%08x) Skip Endpoint Stop Request, Pre Stop Status = @Enum(RTK_status(%u))"
- "endpoint.c:742::@XHCAddrTag(%08x) Endpoint Set TR DQPTR: Invalid stream ID, latest_stream_id=%u, #streams=%u"
- "endpoint.c:755::@XHCAddrTag(%08x) DB Ring to stopped EP"
- "endpoint.c:783::@XHCAddrTag(%08x) Flush Stop EP, completion_code=@Enum(trb_completion_code_t(%u))"
- "endpoint.c:796::@XHCAddrTag(%08x) Warning! endpoint_flush_stop_ep_event_handler received unexpected stop endpoint completion event"
- "main.c:32::XHC firmware started (FW build version: AppleXHCFirmware-242.0.1~1595.t6050)"
```
