# 18.1 (22B5075a) .vs 18.1 (22B82)

## IPSWs

- `iPhone17,1_18.1_22B5075a_Restore.ipsw`
- `iPhone17,1_18.1_22B82_Restore.ipsw`

## Kernel

### Version

| iOS | Version | Build | Date |
| :-- | :------ | :---- | :--- |
| 18.1 *(22B5075a)* | 24.1.0 | 11215.42.1~2 | Mon, 07Oct2024 22:31:15 PDT |
| 18.1 *(22B82)* | 24.1.0 | 11215.42.1~1 | Mon, 07Oct2024 21:14:29 PDT |

### Kexts

#### ❌ Removed (1)

- `com.apple.kec.AppleEncryptedArchive`

#### ⬆️ Updated (11)

<details>
  <summary><i>View Updated</i></summary>

>  `com.apple.driver.AppleBasebandPCIMAVPDP`

```diff

 810.0.0.0.0
   __TEXT.__const: 0x128
-  __TEXT.__cstring: 0x4bd1
-  __TEXT_EXEC.__text: 0x2456c
+  __TEXT.__cstring: 0xcf4
+  __TEXT_EXEC.__text: 0xbf90
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
   __DATA.__common: 0x128
   __DATA.__bss: 0xb0
-  __DATA_CONST.__auth_got: 0x2d8
-  __DATA_CONST.__got: 0x80
+  __DATA_CONST.__auth_got: 0x2b8
+  __DATA_CONST.__got: 0x70
   __DATA_CONST.__mod_init_func: 0x70
   __DATA_CONST.__mod_term_func: 0x38
-  __DATA_CONST.__const: 0x3818
+  __DATA_CONST.__const: 0x3810
   __DATA_CONST.__kalloc_type: 0x400
-  Functions: 363
+  Functions: 364
   Symbols:   0
-  CStrings:  362
+  CStrings:  52
 
CStrings:
+ "1211111212221212111111112111112111111111111121121121121111211211111212222"
+ "12111112122212121111211122222221211111222221212"
+ "12111112122212121212111111111111111111111222222222222222222222222222222222221111111111111111111111111111111111111111111111111111111111111111111111222222222222222221111121122222222221111111111111111222122222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222111111111111111111111111111111112222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222211111111111111112222"
+ "12111112122212121212111111111111111111111222222222222222222222222222222222221111111111111111111111111111111111111111111111111111111111111111111111222222222222222221111121122222222222222222222222212212112"
+ "121111121222121212121111111111111111111112222222222222222222222222222222222211111111111111111111111111111111111111111111111111111111111111111111112222222222222222211111211222222222222222222222222122121121"
- "%06ld.%06d %s::%s: \n"
- "%06ld.%06d %s::%s: %s: --> \n"
- "%06ld.%06d %s::%s: %u commands, pdp:packets: 0:%u 1:%u 2:%u 3:%u 4:%u 5:%u 6:%u 7:%u\n"
- "%06ld.%06d %s::%s: -- Done.\n"
- "%06ld.%06d %s::%s: -- done!\n"
- "%06ld.%06d %s::%s: --done\n"
- "%06ld.%06d %s::%s: Adding Tx pkt meta data failed with 0x%08x\n"
- "%06ld.%06d %s::%s: Avail data indication -- qmap hdr 0x%08x\n"
- "%06ld.%06d %s::%s: Avail data indication raw data 0x%08x %08x %08x %08x\n"
- "%06ld.%06d %s::%s: Avail data timer expired, but interface was closed\n"
- "%06ld.%06d %s::%s: Available data is non-zero, bytes: %u\n"
- "%06ld.%06d %s::%s: Bad DL dump (offset=%llu, remain=%llu)\n"
- "%06ld.%06d %s::%s: Bad RSC header\n"
- "%06ld.%06d %s::%s: Bearer already mapped to Default Service\n"
- "%06ld.%06d %s::%s: Bearer already mapped to Low Latency Service\n"
- "%06ld.%06d %s::%s: Bearer switch already pending, ownerID: %u, bearerID: %u\n"
- "%06ld.%06d %s::%s: Bearer switch complete !\n"
- "%06ld.%06d %s::%s: Bearer switch in progress\n"
- "%06ld.%06d %s::%s: Bearer switch notify!\n"
- "%06ld.%06d %s::%s: Bearer switch request for ownerID: %u, bearer ID: %u, req type: %u\n"
- "%06ld.%06d %s::%s: BearerID: %u not present for OwnerID: %u"
- "%06ld.%06d %s::%s: Blocking outgoing traffic due to IP appender (unit number %u)\n"
- "%06ld.%06d %s::%s: Cmd header: name 0x%02x: type 0x%02x: reserved 0x%04x: trans_id 0x%08x\n"
- "%06ld.%06d %s::%s: Command response raw data 0x%08x %08x %08x %08x %08x\n"
- "%06ld.%06d %s::%s: Creating interface: pdp_qctun\n"
- "%06ld.%06d %s::%s: DFC End Marker Ack already pending for ownerID: %u\n"
- "%06ld.%06d %s::%s: DFC End Marker command invalid length %u\n"
- "%06ld.%06d %s::%s: DFC End Marker command raw data 0x%08x %08x %08x\n"
- "%06ld.%06d %s::%s: DFC Info Query response raw data 0x%08x %08x\n"
- "%06ld.%06d %s::%s: DFC Info query -- qmap hdr 0x%08x\n"
- "%06ld.%06d %s::%s: DFC Info query -- qmap hdr 0x%08x %08x\n"
- "%06ld.%06d %s::%s: DFC Info query for bearer ID: %u, ownerID: %u\n"
- "%06ld.%06d %s::%s: DFC Info query raw data 0x%08x\n"
- "%06ld.%06d %s::%s: DFC Query info response invalid length %u\n"
- "%06ld.%06d %s::%s: DFC notify command invalid length %u\n"
- "%06ld.%06d %s::%s: DFC notify command raw data 0x%08x %08x %08x\n"
- "%06ld.%06d %s::%s: DFC power save mode ack not received!\n"
- "%06ld.%06d %s::%s: DFC_INFO_QUERY response, ignore query response for inactive bearer ownerID: %u, bearer ID: %u, credits: %u\n"
- "%06ld.%06d %s::%s: DFC_INFO_QUERY response, ignore query response for unmapped bearer ownerID: %u, bearer ID: %u, credits: %u\n"
- "%06ld.%06d %s::%s: DL packet dump\n"
- "%06ld.%06d %s::%s: DL packet dump (offset=%llu, length=%u, remain=%llu)\n"
- "%06ld.%06d %s::%s: Data powersave mode command -- qmap hdr 0x%08x\n"
- "%06ld.%06d %s::%s: Data powersave mode command raw data 0x%08x %08x %08x %08x %08x\n"
- "%06ld.%06d %s::%s: Deferring Ack for DFC End Marker\n"
- "%06ld.%06d %s::%s: Delete _CreditsQueue entries for intf: %u\n"
- "%06ld.%06d %s::%s: Duplicate / redundant bearer removed notification for bearerID: %u, ownerID: %u, seq num: %u\n"
- "%06ld.%06d %s::%s: Duplicate DFC_NOTIFY command for bearerID: %u, ownerID: %u, seq num: %u\n"
- "%06ld.%06d %s::%s: Error detected on Modem - removing bearerID: %u\n"
- "%06ld.%06d %s::%s: Failed to create matching dictionary\n"
- "%06ld.%06d %s::%s: Flushing pci service's stage queue pkts to queue set, packetCnt: %u\n"
- "%06ld.%06d %s::%s: Got reset bearers marker: %u for this interface\n"
- "%06ld.%06d %s::%s: Hdr Size:%u interface %u, pkt size %u, padding %u\n"
- "%06ld.%06d %s::%s: IP Appender failed with 0x%08x\n"
- "%06ld.%06d %s::%s: Incorrect bearer mapping state, ownerID: %u, bearerID: %u, current mapped owner: %u\n"
- "%06ld.%06d %s::%s: Inserting at HEAD\n"
- "%06ld.%06d %s::%s: Inserting at Tail\n"
- "%06ld.%06d %s::%s: Inserting before ownerID: %u, bearer ID: %u, credits: %u,\n"
- "%06ld.%06d %s::%s: Interface advisory report: owner %u: payload bytes %u\n"
- "%06ld.%06d %s::%s: Invalid NL pair data length, expected: %u, actual: %u\n"
- "%06ld.%06d %s::%s: Invalid bearer status : %u\n"
- "%06ld.%06d %s::%s: Invalid bearer status: %u, for bearer ID: %u\n"
- "%06ld.%06d %s::%s: Invalid bearer switch request type, req type: %u\n"
- "%06ld.%06d %s::%s: Invalid chksm\n"
- "%06ld.%06d %s::%s: Invalid intf number: %u!\n"
- "%06ld.%06d %s::%s: Invalid number of NLs, received: %u, max: %u\n"
- "%06ld.%06d %s::%s: Invalid number of bearers: %u\n"
- "%06ld.%06d %s::%s: Invalid ownerID : %u\n"
- "%06ld.%06d %s::%s: Invalid ownerID: %u\n"
- "%06ld.%06d %s::%s: Invalid ownerID: %u, bearerID: %u already mapped to ownerID: %u\n"
- "%06ld.%06d %s::%s: Invalid request type: %u\n"
- "%06ld.%06d %s::%s: LL Bearer Switch Ack raw data 0x%08x %08x\n"
- "%06ld.%06d %s::%s: LL Bearer Switch Request Ack invalid length %u != (Header + Payload) size: %u\n"
- "%06ld.%06d %s::%s: LL Bearer Switch Request Ack invalid length %u < Header Size: %u\n"
- "%06ld.%06d %s::%s: LL Bearer Switch Status command, invalid length %u != (Header + Payload) size: %u\n"
- "%06ld.%06d %s::%s: LL Bearer Switch Status raw data 0x%08x %08x\n"
- "%06ld.%06d %s::%s: LQM report: owner %u: payload bytes %u\n"
- "%06ld.%06d %s::%s: NL pair data len (%u), exceeded max len\n"
- "%06ld.%06d %s::%s: NL[%u](Length: %u, chksum map: 0x%x, NumPkts: %u)\n"
- "%06ld.%06d %s::%s: NULL owner!\n"
- "%06ld.%06d %s::%s: No UL pkts queued for ownerID: %u\n"
- "%06ld.%06d %s::%s: No bearer present for this OwnerID: %u\n"
- "%06ld.%06d %s::%s: No bearer present for this ownerID: %u\n"
- "%06ld.%06d %s::%s: No credit update for owner: %u\n"
- "%06ld.%06d %s::%s: PCIe link is down or is going down\n"
- "%06ld.%06d %s::%s: Packet txid: %u, Expected txid: %u\n"
- "%06ld.%06d %s::%s: Packet type is not QMAP control! \n"
- "%06ld.%06d %s::%s: Packet: %p, Txid: %u\n"
- "%06ld.%06d %s::%s: Preparing response: %s\n"
- "%06ld.%06d %s::%s: Previous tail entry - ownerID: %u, bearer ID: %u, credits: %u,\n"
- "%06ld.%06d %s::%s: RSC service: %u\n"
- "%06ld.%06d %s::%s: Received DFC_END_MARKER for ownerID: %u, bearer ID: %u, seqNum: %u\n"
- "%06ld.%06d %s::%s: Received DFC_INFO_QUERY response for ownerID: %u, bearer ID: %u, credits: %u\n"
- "%06ld.%06d %s::%s: Received DFC_NOTIFY for ownerID: %u, bearer ID: %u, credits: %u, seq num: %u, bearer status: %u\n"
- "%06ld.%06d %s::%s: Redundant bearer removed notificaiton, bearer ID: %u already removed\n"
- "%06ld.%06d %s::%s: Removing bearer failed!\n"
- "%06ld.%06d %s::%s: Request Bearer Switch -- qmap cmd hdr 0x%08x %08x\n"
- "%06ld.%06d %s::%s: Request Bearer Switch -- qmap hdr 0x%08x\n"
- "%06ld.%06d %s::%s: Request Bearer Switch raw data 0x%08x %08x\n"
- "%06ld.%06d %s::%s: Sending DFC End Marker Ack for ownerID: %u\n"
- "%06ld.%06d %s::%s: Setting packet buffer base / limit failed: 0x%llx\n"
- "%06ld.%06d %s::%s: Start --\n"
- "%06ld.%06d %s::%s: Start, options 0x%08x --\n"
- "%06ld.%06d %s::%s: Stop queueing pkts - DFC end marker / UL flow switched!\n"
- "%06ld.%06d %s::%s: Tcp Ack Allowed: %u\n"
- "%06ld.%06d %s::%s: Temp failure in switching bearer ID: %u\n"
- "%06ld.%06d %s::%s: Trigger DFC End Marker Ack\n"
- "%06ld.%06d %s::%s: UL packet dump\n"
- "%06ld.%06d %s::%s: Unexpected - bearer info entry is NULL!\n"
- "%06ld.%06d %s::%s: Unexpected Tx\n"
- "%06ld.%06d %s::%s: Unexpected command in RSC channel\n"
- "%06ld.%06d %s::%s: Unexpected control packet for out of band Qmap control service\n"
- "%06ld.%06d %s::%s: Unexpected next header for RSC\n"
- "%06ld.%06d %s::%s: Unexpected pci service ID: %u\n"
- "%06ld.%06d %s::%s: Unknown or unhandled command, name: %u\n"
- "%06ld.%06d %s::%s: Unmapping bearerID: %u from OwnerID: %u\n"
- "%06ld.%06d %s::%s: Unsupported status\n"
- "%06ld.%06d %s::%s: Updated credits for ownerID: %u, credits remaining: %u\n"
- "%06ld.%06d %s::%s: [%u] bearerID: %u, credits: %u\n"
- "%06ld.%06d %s::%s: _rxHEAD: %p, _rxTail: %p\n"
- "%06ld.%06d %s::%s: allowed Tx bytes: %u\n"
- "%06ld.%06d %s::%s: bad command packet size: %u\n"
- "%06ld.%06d %s::%s: bad length %u for link status report payload\n"
- "%06ld.%06d %s::%s: bearer switch ack, bearer ID: %u, status: %u\n"
- "%06ld.%06d %s::%s: bearer switch status, bearer ID: %u, status: %u\n"
- "%06ld.%06d %s::%s: bearer switch was not pending! bearer ID: %u, \n"
- "%06ld.%06d %s::%s: bearer switch was not successful! bearer ID: %u, \n"
- "%06ld.%06d %s::%s: bearer switch was not successful! bearer ID: %u, status: %u \n"
- "%06ld.%06d %s::%s: bytesRead (%llu) != header (%lu) + body (%u)\n"
- "%06ld.%06d %s::%s: cache max reached, dropping packet\n"
- "%06ld.%06d %s::%s: cannot receive interface advisory report for nonexisting owner %u\n"
- "%06ld.%06d %s::%s: cannot receive link status report for nonexisting owner %u\n"
- "%06ld.%06d %s::%s: chain length = %u\n"
- "%06ld.%06d %s::%s: chain length = %u, txid 0x%u --> 0x%u, total DL data %u bytes\n"
- "%06ld.%06d %s::%s: cksmValid: %u, numNLs: %u, incIPID: %u\n"
- "%06ld.%06d %s::%s: close called on an unopened client %p\n"
- "%06ld.%06d %s::%s: closeVal: %u, closeType: %u, contextID: %u\n"
- "%06ld.%06d %s::%s: cmd header: name 0x%02x: type 0x%02x: reserved 0x%04x: trans_id 0x%08x\n"
- "%06ld.%06d %s::%s: cmd version: %u\n"
- "%06ld.%06d %s::%s: command header raw data: 0x%08x 0x%08x\n"
- "%06ld.%06d %s::%s: command name: %u\n"
- "%06ld.%06d %s::%s: consumed:%u\n"
- "%06ld.%06d %s::%s: count %u\n"
- "%06ld.%06d %s::%s: count %u, telescoping limit %u\n"
- "%06ld.%06d %s::%s: count: %u\n"
- "%06ld.%06d %s::%s: dealloc packet %p directly\n"
- "%06ld.%06d %s::%s: device: %p, stateNumber: %lu\n"
- "%06ld.%06d %s::%s: disable soft flow control for pdp_ip%u due to %u pending write bytes\n"
- "%06ld.%06d %s::%s: disabling flow control due to QMAP command\n"
- "%06ld.%06d %s::%s: draining pci service's stage queue pkts to queue set, packetCnt: %u\n"
- "%06ld.%06d %s::%s: duplicate QMAP extension header type (%u)\n"
- "%06ld.%06d %s::%s: enabling flow control due to QMAP command\n"
- "%06ld.%06d %s::%s: enabling flow control for pdp_ip%u due to %u pending Tx bytes\n"
- "%06ld.%06d %s::%s: error 0x%08x\n"
- "%06ld.%06d %s::%s: failed to clone packet\n"
- "%06ld.%06d %s::%s: failed to create Available data zero indication timer\n"
- "%06ld.%06d %s::%s: failed to create Rx queue\n"
- "%06ld.%06d %s::%s: failed to create Tx completion queue\n"
- "%06ld.%06d %s::%s: failed to create Tx queue\n"
- "%06ld.%06d %s::%s: failed to create power save mode timer\n"
- "%06ld.%06d %s::%s: failed to open provider\n"
- "%06ld.%06d %s::%s: failed to set packet limits: 0x%08x\n"
- "%06ld.%06d %s::%s: flow control %s: owner %u: ipFamily %u: sequence 0x%04x: QoS 0x%08x\n"
- "%06ld.%06d %s::%s: flow control command invalid IP family %u\n"
- "%06ld.%06d %s::%s: flow control command invalid length %u\n"
- "%06ld.%06d %s::%s: flow control command raw data 0x%08x %08x\n"
- "%06ld.%06d %s::%s: flow control disable sequence number mismatch (got %u, expected %u)\n"
- "%06ld.%06d %s::%s: flow controlling bearerID: %u, ownerID: %u\n"
- "%06ld.%06d %s::%s: found client, unit %u\n"
- "%06ld.%06d %s::%s: free count: %u\n"
- "%06ld.%06d %s::%s: interface %u not opened yet, packet will be queued\n"
- "%06ld.%06d %s::%s: interface %u, size %u, padding %u, command %u\n"
- "%06ld.%06d %s::%s: interface 0x%p not found\n"
- "%06ld.%06d %s::%s: interface down\n"
- "%06ld.%06d %s::%s: intf %p, count %u\n"
- "%06ld.%06d %s::%s: intf number: %u, open: %u, owner = %p\n"
- "%06ld.%06d %s::%s: invalid interface %d\n"
- "%06ld.%06d %s::%s: invalid length for LQM command, length: %u\n"
- "%06ld.%06d %s::%s: invalid null header\n"
- "%06ld.%06d %s::%s: invoked with packetCount = 0\n"
- "%06ld.%06d %s::%s: kOffPowerState\n"
- "%06ld.%06d %s::%s: kOffPowerState, enable data powersave mode, allow notification: %u\n"
- "%06ld.%06d %s::%s: kOnPowerState, disable data powersave mode\n"
- "%06ld.%06d %s::%s: konPowerState\n"
- "%06ld.%06d %s::%s: last queued pkt completed, trigger DFC end marker Ack for %u\n"
- "%06ld.%06d %s::%s: link status report: owner %u: payload bytes %u\n"
- "%06ld.%06d %s::%s: low latency service: %u\n"
- "%06ld.%06d %s::%s: null header\n"
- "%06ld.%06d %s::%s: out of band QMAP control: %u\n"
- "%06ld.%06d %s::%s: oversize header (%u < %u)\n"
- "%06ld.%06d %s::%s: oversize header (%u < %zu)\n"
- "%06ld.%06d %s::%s: owner %u does not exist, processing command anyway\n"
- "%06ld.%06d %s::%s: owner: %u is inactive\n"
- "%06ld.%06d %s::%s: owner: %u is not active\n"
- "%06ld.%06d %s::%s: owner: %u is not opened yet\n"
- "%06ld.%06d %s::%s: ownerID: %u\n"
- "%06ld.%06d %s::%s: ownerID: %u has no bearer info entry for bearerID: %u\n"
- "%06ld.%06d %s::%s: ownerID: %u was previously flow controlled, updated credits: %u\n"
- "%06ld.%06d %s::%s: ownerID: %u, avail data bytes: %u\n"
- "%06ld.%06d %s::%s: ownerID: %u, bearerID: %u, Active -> Removed\n"
- "%06ld.%06d %s::%s: ownerID: %u, bearerID: %u, Inactive -> Active\n"
- "%06ld.%06d %s::%s: ownerID: %u, bearerID: %u, curr bearer state: %u, new status: %u\n"
- "%06ld.%06d %s::%s: ownerID: %u, bearerID: %u, switchStatus: %u\n"
- "%06ld.%06d %s::%s: ownerID: %u, credits queue...\n"
- "%06ld.%06d %s::%s: packet 0x%p, count: %u\n"
- "%06ld.%06d %s::%s: packet: %p, TxID: %u\n"
- "%06ld.%06d %s::%s: packet: %p, TxID: %u, next TxID: %u, count: %u\n"
- "%06ld.%06d %s::%s: pad bytes (%u) is >= total length (%u)\n"
- "%06ld.%06d %s::%s: pci service not available\n"
- "%06ld.%06d %s::%s: pciService not available\n"
- "%06ld.%06d %s::%s: pdp:packets: 0:%u 1:%u 2:%u 3:%u 4:%u 5:%u 6:%u 7:%u\n"
- "%06ld.%06d %s::%s: pdp_ip%u flow controlled, but continue until soft flow control is enabled\n"
- "%06ld.%06d %s::%s: qmap_control_service not present in plist\n"
- "%06ld.%06d %s::%s: read size too small: %llu\n"
- "%06ld.%06d %s::%s: received ack for Data Powersave Mode Control command\n"
- "%06ld.%06d %s::%s: redundant flow control disable command for owner %u\n"
- "%06ld.%06d %s::%s: redundant flow control enable command for owner %u\n"
- "%06ld.%06d %s::%s: refCon 0x%p, status 0x%x\n"
- "%06ld.%06d %s::%s: refcon: %p, status 0x%x\n"
- "%06ld.%06d %s::%s: refcon: %p, status 0x%x, enqueue: %u\n"
- "%06ld.%06d %s::%s: registering callback for ownerID: %u\n"
- "%06ld.%06d %s::%s: requesting upto: %llu usecs to PM\n"
- "%06ld.%06d %s::%s: residue (%llu) < header (%lu) + body (%u)\n"
- "%06ld.%06d %s::%s: returning free space: %u, service id: %u\n"
- "%06ld.%06d %s::%s: sending data powersave mode, ownerID: %u, enable: %u\n"
- "%06ld.%06d %s::%s: sending response...\n"
- "%06ld.%06d %s::%s: sending response: %s\n"
- "%06ld.%06d %s::%s: sent bytes: %u\n"
- "%06ld.%06d %s::%s: sent bytes: %u, pkt cnt: %u\n"
- "%06ld.%06d %s::%s: setting %u msecs timer\n"
- "%06ld.%06d %s::%s: skipping disable powersave mode, first power on\n"
- "%06ld.%06d %s::%s: soft flow control active on pdp_ip%u\n"
- "%06ld.%06d %s::%s: staged: %u\n"
- "%06ld.%06d %s::%s: super::handleOpen() failed\n!"
- "%06ld.%06d %s::%s: super::open failed\n"
- "%06ld.%06d %s::%s: too many packets in transfer (limit %u), dropping packet\n"
- "%06ld.%06d %s::%s: transfer size %u, interface %u, txid %u\n"
- "%06ld.%06d %s::%s: txid 0x%08x: status 0x%x, packet 0x%p\n"
- "%06ld.%06d %s::%s: txid 0x%x\n"
- "%06ld.%06d %s::%s: unable to get unsent bytes: 0x%x\n"
- "%06ld.%06d %s::%s: unexpected command type %u\n"
- "%06ld.%06d %s::%s: unexpected command type: %u\n"
- "%06ld.%06d %s::%s: unit number %u invalid or nonexistent\n"
- "%06ld.%06d %s::%s: unrecognized QMAP extension header type (%u)\n"
- "%06ld.%06d %s::%s: unsupported command: name 0x%02x: type %u: transactionID 0x%08x\n"
- "%06ld.%06d %s::%s: unsupported flow control QoS 0x%08x\n"
- "%06ld.%06d %s::%s: updating bearer credits failed!\n"
- "%06ld.%06d %s::%s: updating owners in QMAP control intf failed\n"
- "%06ld.%06d %s::%s: waiting for Low Latency service\n"
- "%06ld.%06d %s::%s: waiting for QMAP control service\n"
- "%06ld.%06d %s::%s: waiting for RSC service\n"
- "12111112122212121111111121111121111111111111121121121121111211211111212222"
- "121111121222121211112111222222212111112222212121"
- "121111121222121212121111111111111111111111222222222222222222222222222222222221111111111111111111111111111111111111111111111111111111111111111111111222222222222222221111121122222222221111111111111111222122222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222111111111111111111111111111111112222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222211111111111111112222"
- "121111121222121212121111111111111111111111222222222222222222222222222222222221111111111111111111111111111111111111111111111111111111111111111111111222222222222222221111121122222222222222222222222212212112"
- "1211111212221212121211111111111111111111112222222222222222222222222222222222211111111111111111111111111111111111111111111111111111111111111111111112222222222222222211111211222222222222222222222222122121121"
- "addTxPktMetaData"
- "allocQueues"
- "availDataZeroTimerCompletion"
- "bearerSwitchComplete_block_invoke"
- "closeGated"
- "commandResponse"
- "commandResponse_block_invoke"
- "createRxSubmissionQueue"
- "decodeQMAPHeader"
- "decodeQMAPRSCHeader"
- "disable"
- "discardRxPacket"
- "dumpOwnerCreditsQueue"
- "enable"
- "flowControlAllBearers"
- "free"
- "getAvailData"
- "getOwnerCredits_block_invoke"
- "handleOpen"
- "initWithOptions"
- "openGated"
- "outputComplete"
- "powerSaveModeTimerCompletion"
- "powerStateWillChangeTo"
- "powerStateWillChangeTo_block_invoke"
- "processBearerCreditsGated"
- "processCtrlPacket"
- "processDFCEndMarker"
- "processDFCInfoQuery"
- "processDFCLLSwitchRequest"
- "processDFCLLSwitchStatus"
- "processDFCNotify"
- "processDFCPowerSaveMode"
- "processMavExtCmdAdvisoryReport"
- "processMavExtCmdLQM"
- "queryFlowControlCredits_block_invoke"
- "queryFreeULSpace"
- "queueRxBuffersGated"
- "readComplete"
- "registerBearerSwitchCallback"
- "requestBearerSwitchGated"
- "requestTxGated"
- "resetOwnerCreditsQueue"
- "rxQueueCallbackGated"
- "sendAvailDataIndication_block_invoke"
- "sendDFCEndMarkerAck_block_invoke"
- "sendDataPowerSaveMode_block_invoke"
- "setBearerSwitchPending_block_invoke"
- "setInterfaceOwnerGated"
- "setPowerStateGated"
- "start"
- "terminate"
- "triggerBearerSwitch_block_invoke"
- "triggerRxDequeue_block_invoke"
- "txCompletionCallbackGated"
- "txQueueCallbackGated"
- "updateOwnerCreditsGated_block_invoke"
- "usesQmapControlService"
- "willTerminate"
- "willTerminate_block_invoke"

```

>  `com.apple.driver.AppleOLYHAL`

```diff

 338.1.0.0.0
   __TEXT.__const: 0x7a8
   __TEXT.__cstring: 0x471a
-  __TEXT_EXEC.__text: 0x1cba0
+  __TEXT_EXEC.__text: 0x1cbb8
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x18c
   __DATA.__common: 0x170

```

>  `com.apple.kernel`

```diff

 11215.42.1.0.0
-  __TEXT.__const: 0x383f0
+  __TEXT.__const: 0x38330
   __TEXT.__copyio_vectors: 0xf0
-  __TEXT.__cstring: 0x70bde
+  __TEXT.__cstring: 0x6d6b1
   __TEXT.__os_log: 0x26d15
   __TEXT.__eh_frame: 0x610
   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__mod_init_func: 0x2c8
-  __DATA_CONST.__const: 0xa5f88
+  __DATA_CONST.__const: 0xa5d88
   __DATA_CONST.__hib_const: 0x120
-  __DATA_CONST.__kalloc_type: 0x135c0
+  __DATA_CONST.__kalloc_type: 0x13300
   __DATA_CONST.__kalloc_var: 0x7c60
   __DATA_CONST.__exclaves_bt: 0x60
-  __DATA_CONST.__brk_desc: 0x78
+  __DATA_CONST.__brk_desc: 0x60
   __DATA_SPTM.__const: 0x3c000
   __TEXT_EXEC.__hib_text: 0xc68
-  __TEXT_EXEC.__text: 0x7e90d4
+  __TEXT_EXEC.__text: 0x7d5b9c
   __TEXT_BOOT_EXEC.__bootcode: 0x4cd8
   __KLD.__text: 0x1644
   __LASTDATA_CONST.__mod_init_func: 0x8

   __KLDDATA.__mod_init_func: 0x8
   __KLDDATA.__mod_term_func: 0x8
   __KLDDATA.__bss: 0x1
-  __DATA.__data: 0x185c9
-  __DATA.__lock_grp: 0x5908
+  __DATA.__data: 0x17dc9
+  __DATA.__lock_grp: 0x5858
   __DATA.__percpu: 0x6e30
-  __DATA.__common: 0x58608
+  __DATA.__common: 0x583a8
   __DATA.__bss: 0x95938
   __BOOTDATA.__data: 0x18000
-  __BOOTDATA.__init_entry_set: 0x10a58
+  __BOOTDATA.__init_entry_set: 0x10950
   __BOOTDATA.__init: 0x5b110
   __PRELINK_TEXT.__text: 0x0
   __PRELINK_INFO.__info: 0x0

   __PLK_LLVM_COV.__llvm_covmap: 0x0
   __PLK_LINKEDIT.__data: 0x0
   __LINKINFO.__symbolsets: 0x45557
-  Functions: 20326
+  Functions: 20113
   Symbols:   0
-  CStrings:  17017
+  CStrings:  16732
 
CStrings:
- "\n(kern_coredump_routine) : kern_dump_record_file failed with %d\n"
- "\nBeginning coredump of %s\n"
- "\nBeginning dump of panic region of size 0x%zx\n"
- "\nCore dump took %llu cycles\n"
- " Compressed file length is %llu bytes\n"
- "%"
- "%.12s-cp"
- "%lld..\n"
- "%lu"
- "%qx:%x"
- "%s (during forwarding) returned 0x%x\n"
- "%s (passing along request) returned 0x%x\n"
- "%s kvtophys() for address %p returned NULL\n"
- "%s next stage output failed\n"
- "%s%c%s%c%s%c"
- "%s(%p, %llu, %p) : called with invalid length %llu\n"
- "%s(%p, %llu, %p) : called with too much data, %llu written, %llu left\n"
- "%s() : failed to write data (%llu bytes remaining) :%d\n"
- "%s() : failed to write legacy bin spec version : coredump_save_note_data() returned 0x%x\n"
- "%s() : failed to write mach header : kdp_core_output(%p, %lu, %p) returned error 0x%x\n"
- "%s() : failed to write main bin spec structure : coredump_save_note_data() returned 0x%x\n"
- "%s() : failed to write note %llu of %llu : kdp_core_output() returned  error 0x%x\n"
- "%s() : failed to write sw_vers string : coredump_save_note_data() returned 0x%x\n"
- "%s() : failed to write thread data : kdp_core_output() returned 0x%x\n"
- "%s() : failed to write zero fill padding : kdp_core_output(%p, %llu, NULL) returned 0x%x\n"
- "%s() : found %d expected LC_THREAD (%d)\n"
- "%s() : ran out of space to save threads with %llu of %llu remaining\n"
- "%s() called too many times, %llu note descriptions already recorded\n"
- "%s() called with invalid data_owner\n"
- "%s(): encountered unknown debug header entry %d, including anyway with name '%s'\n"
- "%s(): failed to write load binary spec structure for binary #%d ('%s'): callback returned 0x%x\n"
- "%s(0x%llx, 0x%llx, %p) : called with invalid addresses : start 0x%llx >= end 0x%llx\n"
- "%s(0x%llx, 0x%llx, %p) : called with invalid addresses for 32-bit : start 0x%llx, end 0x%llx\n"
- "%s(0x%llx, 0x%llx, %p) : coredump_save_segment_descriptions() called too many times, %llu segment descriptions already recorded\n"
- "%s(0x%llx, 0x%llx, %p) : failed to write segment %llu of %llu : kdp_core_output(%p, %lu, %p) returned  error 0x%x\n"
- "%s(0x%llx, 0x%llx, %p) : failed to write segment %llu of %llu. kdp_core_output(%p, %lu, %p) returned error %d\n"
- "%s(0x%llx, 0x%llx, %p) : ran out of space to save commands with %llu of %llu remaining\n"
- "%s-%s-%d.%d.%d.%d-%x%s"
- "%s/%s"
- "%s: cannot exclude region starting at %p with size %zu (not page aligned) @%s:%d"
- "%s: cannot exclude region starting at %p with size %zu (zero or overflowing size) @%s:%d"
- "%s: context allocation failure\n"
- "%s: no task is set\n"
- "%s: skipping inactive task\n"
- "%s: skipping kernel because excluded regions list is locked\n"
- "%s: skipping locked task\n"
- "%s: skipping task with locked vm map\n"
- "%s: vm map traversal failed: %d\n"
- "(%s) : coredump_init failed with %d\n"
- "(%s) : coredump_save_note_description returned %d while writing binary info LC_NOTE description"
- "(%s) : get_summary failed with %d\n"
- "(%s) : header size not populated after coredump_get_summary\n"
- "(%s) : kcc_coredump_save_note_data failed with 0x%x\n"
- "(%s) : kcc_coredump_save_note_data returned without all note data written, %llu of %llu remaining\n"
- "(%s) : kcc_coredump_save_note_descriptions failed with %d\n"
- "(%s) : kcc_coredump_save_sw_vers failed with 0x%x\n"
- "(%s) : kcc_coredump_save_sw_vers_detail_cb failed with 0x%x\n"
- "(%s) : save_note_descriptions returned without all note descriptions written, %llu of %llu remaining\n"
- "(%s) : save_note_note_summary failed with %d\n"
- "(%s) : save_segment_descriptions failed with %d\n"
- "(%s) : save_segment_descriptions returned without all segment descriptions written, %llu of %llu remaining\n"
- "(%s) : save_thread_state failed with %d\n"
- "(%s) : save_thread_state returned without all thread descriptions written, %llu of %llu remaining\n"
- "(aea_read_callback) next stage read proc returned 0x%x\n"
- "(aea_stage_outproc) aea_close() returned %d\n"
- "(aea_stage_outproc) aea_open() returned %d\n"
- "(aea_stage_outproc) aea_write() returned %zd\n"
- "(aea_stage_reset) aea_close() returned %d\n"
- "(aea_write_callback) next stage outproc returned 0x%x\n"
- "(disk_stage_read) IOPolledFileRead(%llu) returned 0x%x\n"
- "(disk_stage_read) IOPolledFileSeek(0x%llx) returned 0x%x\n"
- "(disk_stage_read) IOPolledFileWrite (during seek) returned 0x%x\n"
- "(disk_stage_read) Kickstarting IOPolledFileRead(0) returned 0x%x\n"
- "(disk_stage_write) IOPolledFileSeek(0x%llx) returned 0x%x\n"
- "(disk_stage_write) IOPolledFileWrite (during final flush) returned 0x%x\n"
- "(disk_stage_write) IOPolledFileWrite(gIOPolledCoreFileVars, %p, 0x%llx, NULL) returned 0x%x\n"
- "(disk_stage_write) disk_stage_read (during final chunk seek) returned 0x%x\n"
- "(disk_stage_write) disk_stage_read (during seek) returned 0x%x\n"
- "(do_kern_dump close) outproc(KDP_EOF, NULL, 0, 0) returned 0x%x\n"
- "(do_kern_dump coredump log) outproc(KDP_DATA, NULL, %lu, %p) returned 0x%x\n"
- "(do_kern_dump paniclog) outproc(KDP_DATA, NULL, %lu, %p) returned 0x%x\n"
- "(do_kern_dump seek begin) outproc(KDP_SEEK, NULL, %lu, %p) foffset = 0x%llx returned 0x%x\n"
- "(do_kern_dump seek logfile) outproc(KDP_SEEK, NULL, %lu, %p) foffset = 0x%llx returned 0x%x\n"
- "(do_kern_dump write public key) returned 0x%x\n"
- "(kdp_core_output) outproc(KDP_DATA, NULL, 0x%llx, %p) returned 0x%x\n"
- "(kdp_reset_output_vars) Encryption requested, is unavailable, and enforcement is active. Skipping current core.\n"
- "(kern_coredump_routine) : failed to flush final core data : kdp_core_output(%p, 0, NULL) returned 0x%x\n"
- "(kern_coredump_routine) : failed to write zero fill padding (%llu bytes remaining) : kdp_core_output(%p, %llu, NULL) returned 0x%x\n"
- "(kern_coredump_routine) : save_segment_data returned without all segment data written, %llu of %llu remaining\n"
- "(kern_dump_seek_to_next_file) outproc(KDP_SEEK, NULL, %lu, %p) foffset = 0x%llx returned 0x%x\n"
- "(kern_dump_update_header) outproc data flush returned 0x%x\n"
- "(kern_dump_update_header) outproc explicit flush returned 0x%x\n"
- "(kern_dump_update_header) outproc(KDP_DATA, NULL, %lu, %p) returned 0x%x\n"
- "(kern_dump_update_header) outproc(KDP_SEEK, NULL, %lu, %p) foffset = 0x%llx returned 0x%x\n"
- "(kern_dump_write_public_key) outproc data flush returned 0x%x\n"
- "(kern_dump_write_public_key) outproc explicit flush returned 0x%x\n"
- "(kern_dump_write_public_key) outproc(KDP_DATA, NULL, %llu, NULL) returned 0x%x\n"
- "(kern_dump_write_public_key) outproc(KDP_DATA, NULL, %u, %p) returned 0x%x\n"
- "(kern_dump_write_public_key) outproc(KDP_SEEK, NULL, %lu, %p) foffset = 0x%llx returned 0x%x\n"
- "(zlib_zoutput) outproc(KDP_DATA, NULL, 0x%x, %p) returned 0x%x\n"
- ".gz"
- "/cores/core.%d"
- "/private/preboot/kernelcore"
- "/private/var/cores"
- "/private/var/dextcores"
- "/private/var/vm/kernelcore"
- "100.."
- "111222212222222222222112"
- "121212112"
- "; UUID="
- "; stext="
- "A dump server was not specified in the boot-args, terminating kernel core dump.\n"
- "Attempting connection to panic server configured at IP %s, port %d\n"
- "Boot-args specify %d MB kernel corefile\n"
- "Corefile is not yet initialized. Cannot write a coredump to disk\n"
- "Couldn't retrieve volume status. Error %d\n"
- "Detected remote error, terminating...\n"
- "Detected stale/invalid seq num. Expected: %d, received %d\n"
- "Done\nCoredump complete of %s, dumped %llu segments (%llu bytes), %llu threads (%llu bytes) overall uncompressed file length %llu bytes."
- "EOF Flush: Detected stale/invalid seq num. Expected: %d, received %d\n"
- "Error: No transport device registered for kernel crashdump\n"
- "Failed to %s the corefile. Error %d\n"
- "Failed to dump coprocessor cores\n"
- "Failed to dump userspace process cores\n"
- "Failed to flush panic region data : kdp_core_output(%p, 0, NULL) returned 0x%x\n"
- "Failed to open corefile of size %llu MB (low disk space)\n"
- "Failed to open corefile of size %llu MB (returned error 0x%x)\n"
- "Failed to open the corefile. Error %d\n"
- "Failed to record panic region in corefile header, kern_dump_record_file returned 0x%x\n"
- "Failed to seek to beginning of next core\n"
- "Failed to seek to panic region file offset 0x%llx, kern_dump_seek_to_next_file returned 0x%x\n"
- "Failed to write panic region to file, kdp_coreoutput(outstate, %zu, %p) returned 0x%x\n"
- "IOPolledFileFlush() returned 0x%x\n"
- "IOPolledFileFlush(0x%p) : IOStartPolledIO(0x%p, kIOPolledFlush, 0, 0, 0) returned 0x%x\n"
- "IOPolledFilePollersClose (during EOF) returned 0x%x\n"
- "IOPolledFilePollersOpen returned 0x%x\n"
- "IOPolledFilePollersSetup for corefile failed with error: 0x%x\n"
- "IOPolledFilePollersSetup(%d) error 0x%x\n"
- "IOPolledFileSeek(0x%llx) returned 0x%x\n"
- "IOPolledFileSeek(gIOPolledCoreFileVars, 0) returned 0x%x\n"
- "IOPolledFileSeek: called to seek to 0x%llx greater than file size of 0x%llx\n"
- "IOPolledFileWrite (during EOF) returned 0x%x\n"
- "IOPolledFileWrite (during seek) returned 0x%x\n"
- "IOPolledFileWrite(0x%p, 0x%p, %llu, 0x%p) : IOStartPolledIO(0x%p, kIOPolledWrite, %llu, 0x%llx, %d) returned 0x%x\n"
- "IOPolledFileWrite(gIOPolledCoreFileVars, %p, 0x%llx, NULL) returned 0x%x\n"
- "IOPolledInterface::checkForWork[%d] 0x%x\n"
- "IOPolledInterface::close[%d] 0x%x\n"
- "IOPolledInterface::ioStatus 0x%x\n"
- "IOPolledInterface::open[%d] 0x%x\n"
- "IOPolledInterface::probe[%d] 0x%x\n"
- "IOPolledInterface::startIO[%d] 0x%x\n"
- "IOPolledInterfaceActive"
- "IOPolledInterfaceStack"
- "KDPCoreStageInit"
- "Kernel map size is %llu\n"
- "Kernel timed out waiting for hardware debugger to update handshake structure."
- "LZ4 stage is not yet initialized. Cannot write a coredump to disk\n"
- "No contact in %d seconds\n"
- "Opened corefile of size %llu MB\n"
- "Opened file %s, size %qd, extents %ld, maxio %qx ssd %d\n"
- "Original panic string:\n"
- "Preferred Block Size"
- "Recorded panic region in corefile at offset 0x%llx, compressed to %llu bytes\n"
- "Resolved %s's (or proxy's) link level address\n"
- "Routing through specified router IP %s (%d)\n"
- "Sending write request for %s\n"
- "Set a new encryption key for coredumps"
- "Setting coredump status as done!\n"
- "Skipping coredump\n"
- "Skipping panic region dump\n"
- "Skipping userspace coredump, coredump list is locked\n"
- "System dump aborted.\n"
- "Transmitting kernel state, please wait:\n"
- "Transmitting packets to link level address: %02x:%02x:%02x:%02x:%02x:%02x\n"
- "Transmitting panic log, please wait: "
- "Transmitting system log, please wait: "
- "Unable to create core header packet.\n"
- "Unable to retrieve range for root memory device %d\n"
- "Unknown format character %c in `%s'\n"
- "Volume is low on space. Not allocating kernel corefile.\n"
- "Waiting for hardware shared memory debugger, handshake structure is at virt: %p, phys %p\n"
- "We were in the middle of initializing LZ4 stage. Cannot write a coredump to disk\n"
- "We were in the middle of initializing encryption. Marking it as unavailable\n"
- "We were in the middle of initializing the disk stage. Cannot write a coredump to disk\n"
- "Writing local cores...\n"
- "ZERR %d\n"
- "Zlib stage is not initialized. Cannot write a coredump to shared memory\n"
- "Zlib stage is not initialized. Cannot write a coredump to the network\n"
- "_kdp_ipstr"
- "_panicd_corename"
- "_panicd_ip"
- "_router_ip"
- "addrable bits"
- "apple_encrypted_archive interface registration callback is already set @%s:%d"
- "buffer_stage_outproc (during flush) returned 0x%x\n"
- "buffer_stage_outproc (during forwarding) returned 0x%x\n"
- "com.apple.private.coredump-encryption-key"
- "com.apple.private.custom-coredump-location"
- "com.apple.private.enable-coredump-on-panic-seed-privacy-approved"
- "com.apple.private.security.file-unencrypt-access"
- "compression interface registration callback is already set @%s:%d"
- "coredump"
- "coredump_encryption"
- "coredump_encryption_key"
- "coredump_init returned KERN_NODE_DOWN, skipping this core\n"
- "coredump_save_note_data"
- "coredump_save_note_description"
- "coredump_save_segment_data"
- "coredump_save_segment_data failed with %d\n"
- "coredump_save_segment_descriptions"
- "coredump_save_summary"
- "coredump_save_sw_vers"
- "coredump_save_sw_vers_legacy"
- "coredump_save_thread_state"
- "corefile"
- "corefile path selection in device-tree is not one of the allowed values: %s, Using default %s\n"
- "corefile path selection in device-tree was set to: %s (value: %s)\n"
- "corefile_size_mb"
- "custom"
- "drivercorefile"
- "dumpinfo does not fit into KDP packet.\n"
- "error 0x%x from IOGetHibernationCryptKey\n"
- "error 0x%x opening polled file\n"
- "handshake structure not initialized\n"
- "hwm_user_cores"
- "inet_aton() failed interpreting %s as a panic server IP\n"
- "inet_aton() failed interpreting %s as an IP\n"
- "inline call to debugger(machine_startup)"
- "kdp panic: %s"
- "kdp_core.c"
- "kdp_core_exclude_region"
- "kdp_corefile"
- "kdp_crashdump_pkt_size"
- "kdp_ip_addr"
- "kdp_panic_dump: unexpected pending input packet"
- "kdp_poll"
- "kdp_raise_exception"
- "kdp_reply: no input packet"
- "kdp_send: no input packet"
- "kdp_send: packet too large (%d > %u)"
- "kdp_send_crashdump_data returned 0x%x\n"
- "kdp_send_crashdump_pkt failed with error %d\n"
- "kdp_set_dump_info: Skipping invalid panicd port %d (using %d)\n"
- "kern ver str"
- "kern_coredump_routine"
- "kern_dump_init"
- "kern_dump_save_note_data"
- "kern_open_file_for_direct_io took %qd ms\n"
- "kernel-core-dump-location"
- "load binary"
- "main bin spec"
- "memory_backing_aware_buffer_stage_outproc"
- "misaligned file pos %qx\n"
- "octet"
- "outproc(KDP_WRQ, NULL, 0, NULL) returned 0x%x\n"
- "panic context"
- "panic_region"
- "panicd_port"
- "paniclog"
- "pid %ld (%s), uid (%u): corename is too long\n"
- "pid %ld (%s), uid (%u): unexpected end of string after %% token\n"
- "polled file major %d, minor %d, blocksize %ld, pollers %d\n"
- "preboot"
- "progress_notify_stage_outproc"
- "read from"
- "save_seg_data: pmap traversal failed: %d\n"
- "save_seg_desc: pmap traversal failed: %d\n"
- "save_summary: pmap traversal failed: %d\n"
- "secure_core: Unable to seek to the start of file: %d\n"
- "site.IOPolledFileIOVars"
- "site.struct kern_userspace_coredump_context"
- "site.typeof(*data)"
- "site.typeof(*region)"
- "skipping local kernel core because core file could not be opened prior to panic (mode : 0x%x, error : 0x%x)\n"
- "skipping local kernel core because the SPTM is in INTERRUPTED state and can't support core dump generation\n"
- "skipping local kernel core because the SPTM is in PANIC state and can't support core dump generation\n"
- "sugid_coredump"
- "systemlog"
- "user_dump_init"
- "user_dump_save_seg_descriptions"
- "user_dump_save_segment_data"
- "user_dump_save_summary"
- "write to"
- "xnu"
- "xnu-"

```

>  `com.apple.driver.AppleAOPAudio`

```diff

   __TEXT.__cstring: 0xc591
   __TEXT.__const: 0x136
   __TEXT.__os_log: 0xf
-  __TEXT_EXEC.__text: 0x32934
+  __TEXT_EXEC.__text: 0x32948
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x2f0
   __DATA.__common: 0x660
   __DATA.__bss: 0x49
-  __DATA_CONST.__auth_got: 0x318
+  __DATA_CONST.__auth_got: 0x328
   __DATA_CONST.__got: 0xe8
   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__mod_init_func: 0xe8
CStrings:
+ "18:25:23"
+ "18:25:29"
+ "Oct 11 2024"
- "22:03:13"
- "22:03:23"
- "Oct 10 2024"

```

>  `com.apple.driver.AppleAVD`

```diff

 807.0.0.0.0
-  __TEXT.__const: 0x9a8c9
-  __TEXT.__cstring: 0x5277
-  __TEXT.__os_log: 0x12f18
-  __TEXT_EXEC.__text: 0x45574
+  __TEXT.__const: 0xc5ac9
+  __TEXT.__os_log: 0x143ec
+  __TEXT.__cstring: 0x5391
+  __TEXT_EXEC.__text: 0x4bba4
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x12dc
   __DATA.__common: 0x78

   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__mod_init_func: 0x10
   __DATA_CONST.__mod_term_func: 0x10
-  __DATA_CONST.__const: 0x2d08
-  __DATA_CONST.__kalloc_var: 0xbe0
-  __DATA_CONST.__kalloc_type: 0x2600
-  Functions: 1415
+  __DATA_CONST.__const: 0x3208
+  __DATA_CONST.__kalloc_type: 0x2a00
+  __DATA_CONST.__kalloc_var: 0xc80
+  Functions: 1563
   Symbols:   0
-  CStrings:  1459
+  CStrings:  1472
 
CStrings:
+ "%s(): DKey physical addr = 0x%llx\n"
+ "122211112112112"
+ "CAvdApCommHibiscus"
+ "CAvdApCommThyme"
+ "CAvdMcpuHibiscus"
+ "CAvdMcpuThyme"
+ "site.CAvdApCommHibiscus"
+ "site.CAvdApCommThyme"
+ "site.CAvdMcpuHibiscus"
+ "site.CAvdMcpuThyme"
+ "site.CAvdWrapCtrlHibiscus"
+ "site.CPriorityQueueHibiscus"
+ "site.CPriorityQueueThyme"

```

>  `com.apple.driver.AppleBasebandPCI`

```diff

 810.0.0.0.0
-  __TEXT.__cstring: 0xc286
-  __TEXT.__const: 0x5009
-  __TEXT_EXEC.__text: 0x88dd0
+  __TEXT.__cstring: 0x3809
+  __TEXT.__const: 0x4f69
+  __TEXT_EXEC.__text: 0x48aec
   __TEXT_EXEC.__auth_stubs: 0x0
-  __DATA.__data: 0x3f8
-  __DATA.__common: 0x648
-  __DATA.__bss: 0x3048
-  __DATA_CONST.__auth_got: 0x620
-  __DATA_CONST.__got: 0x180
+  __DATA.__data: 0x33c
+  __DATA.__common: 0x5a0
+  __DATA.__bss: 0x2e50
+  __DATA_CONST.__auth_got: 0x560
+  __DATA_CONST.__got: 0x178
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__mod_init_func: 0x1350
-  __DATA_CONST.__mod_term_func: 0xf0
-  __DATA_CONST.__const: 0xfeb8
-  __DATA_CONST.__kalloc_type: 0x1d80
-  __DATA_CONST.__kalloc_var: 0x690
-  Functions: 2403
+  __DATA_CONST.__mod_init_func: 0x12f0
+  __DATA_CONST.__mod_term_func: 0xd0
+  __DATA_CONST.__const: 0xf108
+  __DATA_CONST.__kalloc_type: 0x1980
+  __DATA_CONST.__kalloc_var: 0x550
+  Functions: 2229
   Symbols:   0
-  CStrings:  1371
+  CStrings:  446
 
CStrings:
+ "121111121222121211111111211111211111111111112112112112111121121111121"
+ "1211111212221212111111112111112111111111111121121121121111211211111212"
+ "12111112122212121111211122222221211111222221212"
+ "12111112122212121211111111111111111111112212212222111111111222"
+ "1211111212221212121211111111111111111111122222222222222222222222222222222222111111111111111111111111111111111111111111111111111111111111111111111122222222222222222111112112222222"
- "\t%06ld.%06d %s %llx\n"
- "%02x %02x %02x %02x %02x %02x %02x %02x %02x %02x %02x %02x %02x %02x %02x %02x"
- "%06ld.%06d %s::%s: \n"
- "%06ld.%06d %s::%s:  --done\n"
- "%06ld.%06d %s::%s:  MSI owner cannot be NULL\n"
- "%06ld.%06d %s::%s:  MSI owner or handler cannot be NULL\n"
- "%06ld.%06d %s::%s:  PDP manager registration with IP Appender failed\n"
- "%06ld.%06d %s::%s:  Type= %s\n HwClass= %s\n HwError= %s\n IsWrite= %s\n HwStatus= %#llX\n SID= %#llx\n Address= %#llx\n"
- "%06ld.%06d %s::%s:  qctun interface tx slot count: %u\n"
- "%06ld.%06d %s::%s: \"%s\" not found in plist\n"
- "%06ld.%06d %s::%s: %02x %02x %02x %02x %02x %02x %02x %02x %02x %02x %02x %02x %02x %02x %02x %02x\n"
- "%06ld.%06d %s::%s: %d\n"
- "%06ld.%06d %s::%s: %s\n"
- "%06ld.%06d %s::%s: %s -> %s\n"
- "%06ld.%06d %s::%s: %s TCP packet: len %u, seq %u, ack %u\n"
- "%06ld.%06d %s::%s: %s override\n"
- "%06ld.%06d %s::%s: %s rx slot count %u\n"
- "%06ld.%06d %s::%s: %s tx slot count %u\n"
- "%06ld.%06d %s::%s: %s%02x %02x %02x %02x %02x %02x %02x %02x %02x %02x %02x %02x %02x %02x %02x %02x\n"
- "%06ld.%06d %s::%s: %s%s\n"
- "%06ld.%06d %s::%s: %s: --> \n"
- "%06ld.%06d %s::%s: %u\n"
- "%06ld.%06d %s::%s: (async) failed client is not attached\n"
- "%06ld.%06d %s::%s: (async) failed to create memory decriptor\n"
- "%06ld.%06d %s::%s: (async) failed to prepare image command\n"
- "%06ld.%06d %s::%s: (async) failed to prepare memory command\n"
- "%06ld.%06d %s::%s: (async) returned 0x%x\n"
- "%06ld.%06d %s::%s: (sync < 4K) failed client is not attached\n"
- "%06ld.%06d %s::%s: (sync < 4K) failed to create memory decriptor\n"
- "%06ld.%06d %s::%s: (sync < 4K) failed to prepare image command\n"
- "%06ld.%06d %s::%s: (sync < 4K) failed to prepare memory command\n"
- "%06ld.%06d %s::%s: (sync < 4K) returned 0x%x\n"
- "%06ld.%06d %s::%s: (sync > 4K) failed client is not attached\n"
- "%06ld.%06d %s::%s: (sync > 4K) failed to prepare image command\n"
- "%06ld.%06d %s::%s: (sync > 4K) failed to prepare memory command\n"
- "%06ld.%06d %s::%s: (sync > 4K) no memory decriptor\n"
- "%06ld.%06d %s::%s: (sync > 4K) returned 0x%x\n"
- "%06ld.%06d %s::%s: +\n"
- "%06ld.%06d %s::%s: -\n"
- "%06ld.%06d %s::%s: -- done\n"
- "%06ld.%06d %s::%s: -- done %u\n"
- "%06ld.%06d %s::%s: --done\n"
- "%06ld.%06d %s::%s: AER was already registered\n"
- "%06ld.%06d %s::%s: ASPML1 disabled on endpoint\n"
- "%06ld.%06d %s::%s: ASPML1 disabled on root port\n"
- "%06ld.%06d %s::%s: AppleBasebandPCI workloop onThread %u, inGate %u\n"
- "%06ld.%06d %s::%s: AppleBasebandPCIControl workloop onThread %u, inGate %u\n"
- "%06ld.%06d %s::%s: Base Rx slot count not found in plist\n"
- "%06ld.%06d %s::%s: Base Tx slot count not found in plist\n"
- "%06ld.%06d %s::%s: Bearer switch trigger failed, ret: 0x%08x\n"
- "%06ld.%06d %s::%s: Bearer switch unsupported for this serviceID: %u\n"
- "%06ld.%06d %s::%s: Client lacks entitlement\n"
- "%06ld.%06d %s::%s: Closing pci service: %p\n"
- "%06ld.%06d %s::%s: Could not open PCI service\n"
- "%06ld.%06d %s::%s: Created qctun interface, pService: %p\n"
- "%06ld.%06d %s::%s: Creating QueueSet failed, index: %u\n"
- "%06ld.%06d %s::%s: Creating logical link failed\n"
- "%06ld.%06d %s::%s: Creating qctun interface\n"
- "%06ld.%06d %s::%s: Creating queue sets for logical link failed\n"
- "%06ld.%06d %s::%s: DART error handler registeration failed!, ret: 0x%08x\n"
- "%06ld.%06d %s::%s: DART window: 0x%llx --> 0x%llx\n"
- "%06ld.%06d %s::%s: DL limit set to %u\n"
- "%06ld.%06d %s::%s: De-Allocate pkts directly to pool, dir: %lu\n"
- "%06ld.%06d %s::%s: Default pci service not published! enabled: %u, shouldEnable: %u\n"
- "%06ld.%06d %s::%s: Default soft flow control thresholds: on %u, off %u\n"
- "%06ld.%06d %s::%s: Device Status/Control register: 0x%lx, isPending: %u\n"
- "%06ld.%06d %s::%s: DeviceCtl 0x%08x DeviceStatus 0x%08x LinkStatus 0x%08x\n"
- "%06ld.%06d %s::%s: Enqueue failed, dir: %u, ret: 0x%08x\n"
- "%06ld.%06d %s::%s: Failed to allocate memory for interface advisory report\n"
- "%06ld.%06d %s::%s: Failed to calculate qctun buffer pool capacity!\n"
- "%06ld.%06d %s::%s: Failed to create Create Dedicated Queue Set\n"
- "%06ld.%06d %s::%s: Failed to create Create Default Queue Set\n"
- "%06ld.%06d %s::%s: Failed to create logical link!\n"
- "%06ld.%06d %s::%s: Failed to create/attach interface, 0x%x\n"
- "%06ld.%06d %s::%s: Failed to get Transaction Pending bit, ret: 0x%llx\n"
- "%06ld.%06d %s::%s: Failed to get device reset state!\n"
- "%06ld.%06d %s::%s: Failed to read AER Capability Structure\n"
- "%06ld.%06d %s::%s: Failed to read PCIe Express Capability Structure\n"
- "%06ld.%06d %s::%s: Flow control service not active\n"
- "%06ld.%06d %s::%s: Getting BB reset state failed\n"
- "%06ld.%06d %s::%s: HMAP VSEC regs(@0x%x)= 0x%x\n"
- "%06ld.%06d %s::%s: HMAP capability not found\n"
- "%06ld.%06d %s::%s: HeaderLog 0 to 3 0x%08x 0x%08x 0x%x 0x%08x\n"
- "%06ld.%06d %s::%s: IOMemoryDescriptor %p\n"
- "%06ld.%06d %s::%s: IOMemoryDescriptor %p, info 0x%llx\n"
- "%06ld.%06d %s::%s: IOSkywalkFamily querying free space, interface: %u, returning: %u\n"
- "%06ld.%06d %s::%s: IPAppender message, message: 0x%u\n"
- "%06ld.%06d %s::%s: Init failed, intf: %p, manager: %p\n"
- "%06ld.%06d %s::%s: Interface non-existent interface ID: %u\n"
- "%06ld.%06d %s::%s: Interface: %u, Rx pkt compl cnt: %lu\n"
- "%06ld.%06d %s::%s: Interface: %u, Tx pkt compl cnt: %lu\n"
- "%06ld.%06d %s::%s: Invalid POSTROM link speed setting, will use defaults\n"
- "%06ld.%06d %s::%s: Invalid ROM link speed setting, will use defaults\n"
- "%06ld.%06d %s::%s: Invalid bearer ID\n"
- "%06ld.%06d %s::%s: Invalid data service: %u\n"
- "%06ld.%06d %s::%s: Invalid direction, dir: %u\n"
- "%06ld.%06d %s::%s: Invalid direction, direction: %u\n"
- "%06ld.%06d %s::%s: Invalid filter rule, descriptor type: \n"
- "%06ld.%06d %s::%s: Invalid interface ID: %u\n"
- "%06ld.%06d %s::%s: Invalid payload length, expected: %u, received: %u\n"
- "%06ld.%06d %s::%s: Invalid service ID: %u\n"
- "%06ld.%06d %s::%s: L1SS control 1 reg: 0x%x\n"
- "%06ld.%06d %s::%s: L1SS control 2 reg: 0x%x\n"
- "%06ld.%06d %s::%s: Logical link NOT supported!\n"
- "%06ld.%06d %s::%s: Low Latency data NOT supported!\n"
- "%06ld.%06d %s::%s: MSI address 0x%x\n"
- "%06ld.%06d %s::%s: MSI capability not found\n"
- "%06ld.%06d %s::%s: MSI registration failed with pci service, ret: 0x%08x\n"
- "%06ld.%06d %s::%s: MSI registration for index %u already exists!\n"
- "%06ld.%06d %s::%s: Mapped bearer ID: %u, queueSetID: 0x%llx\n"
- "%06ld.%06d %s::%s: NOT EOT, bail! status 0x%x, size %u, eot %d\n"
- "%06ld.%06d %s::%s: NULL input argument(s)\n"
- "%06ld.%06d %s::%s: NULL logical link\n"
- "%06ld.%06d %s::%s: NULL message argument\n"
- "%06ld.%06d %s::%s: NULL output arguments\n"
- "%06ld.%06d %s::%s: NULL payload\n"
- "%06ld.%06d %s::%s: NULL traffic descriptor\n"
- "%06ld.%06d %s::%s: Network stack rejected link status report: 0x%x\n"
- "%06ld.%06d %s::%s: Not a valid PCI service\n"
- "%06ld.%06d %s::%s: Not in low power, bailing!\n"
- "%06ld.%06d %s::%s: Not supported for non logical link interfaces\n"
- "%06ld.%06d %s::%s: Opened successfully! _pciService: %p\n"
- "%06ld.%06d %s::%s: Opening PCI data service failed, ret: 0x%08x\n"
- "%06ld.%06d %s::%s: Opening _pciService: %p\n"
- "%06ld.%06d %s::%s: Opening pci service: %p\n"
- "%06ld.%06d %s::%s: PCI notification\n"
- "%06ld.%06d %s::%s: PCI service to switch not active, service ID: %u\n"
- "%06ld.%06d %s::%s: PCIE capability not found\n"
- "%06ld.%06d %s::%s: PCIe link is down or is going down\n"
- "%06ld.%06d %s::%s: PDP event oob allocation, check for potential flaw\n"
- "%06ld.%06d %s::%s: PDP manager service not active\n"
- "%06ld.%06d %s::%s: PDP manager stopped\n"
- "%06ld.%06d %s::%s: POSTROM link speed overridden to: %u\n"
- "%06ld.%06d %s::%s: Packet dump\n"
- "%06ld.%06d %s::%s: Queue Set ID: %u\n"
- "%06ld.%06d %s::%s: ROM link speed overridden to: %u\n"
- "%06ld.%06d %s::%s: Read config space link speed: %u\n"
- "%06ld.%06d %s::%s: Received AER, Config Reg Space Dump : UnCorErrStat 0x%08x CorrErrStat 0x%08x AERCapCtl 0x%08x\n"
- "%06ld.%06d %s::%s: Removed region ID: %u from list\n"
- "%06ld.%06d %s::%s: Reporting interface advisory failed, ret: 0x%08x %u\n"
- "%06ld.%06d %s::%s: Returning packet: %p\n"
- "%06ld.%06d %s::%s: Rx SubQ finalize failed, ret: 0x%llx\n"
- "%06ld.%06d %s::%s: Rx dequeue request\n"
- "%06ld.%06d %s::%s: Rx pkt -  Sub cnt: %u, Compl cnt: %lu\n"
- "%06ld.%06d %s::%s: Rx pkt compl cnt: %lu\n"
- "%06ld.%06d %s::%s: Rx subQ not enabled\n"
- "%06ld.%06d %s::%s: Rx, default queueset: %u\n"
- "%06ld.%06d %s::%s: Setting link control2 to: 0x%08x, new target link speed: %u\n"
- "%06ld.%06d %s::%s: Skip creating qctun intf, qctun_enabled: %u\n"
- "%06ld.%06d %s::%s: Skip dedicated bearer switch for IMS\n"
- "%06ld.%06d %s::%s: Skip queue set disable for IMS\n"
- "%06ld.%06d %s::%s: Skip service id: %u, not a data pci service\n"
- "%06ld.%06d %s::%s: Soft flow control off: %u\n"
- "%06ld.%06d %s::%s: Soft flow control on: %u\n"
- "%06ld.%06d %s::%s: TBD: HMAP MSI-X support\n"
- "%06ld.%06d %s::%s: Timout waiting for bridge to power off! Continuing with potentially unsafe port disable.\n"
- "%06ld.%06d %s::%s: Transaction Pending bit cleared (count: %u)\n"
- "%06ld.%06d %s::%s: Transaction Pending bit poll timed out\n"
- "%06ld.%06d %s::%s: Trigger MSI failed - No event source\n"
- "%06ld.%06d %s::%s: Tx pkt -  Sub cnt: %u, Compl cnt: %lu\n"
- "%06ld.%06d %s::%s: Tx pkt compl cnt: %lu\n"
- "%06ld.%06d %s::%s: Tx subQ not enabled\n"
- "%06ld.%06d %s::%s: Tx, default queueset: %u\n"
- "%06ld.%06d %s::%s: Unable to find the mapped queue set, bearer ID: %u, isDefaultBearer: %u !\n"
- "%06ld.%06d %s::%s: Unable to map to queue set! bearer ID: %u, isDefaultBearer: %u\n"
- "%06ld.%06d %s::%s: Unmapping bearer ID: %u from queue set failed\n"
- "%06ld.%06d %s::%s: Unsupported direction: %u"
- "%06ld.%06d %s::%s: Unsupported direction: %u\n"
- "%06ld.%06d %s::%s: Unsupported notification type: %u\n"
- "%06ld.%06d %s::%s: VSEC ID at offset 0x%x matched HMAP 0x%x\n"
- "%06ld.%06d %s::%s: VSEC ID at offset 0x%x not matched HMAP. Expected 0x0024, found 0x%x\n"
- "%06ld.%06d %s::%s: _asyncMode 0x%08x, asyncMode 0x%08x, arg1 %p\n"
- "%06ld.%06d %s::%s: _enabled: %u\n"
- "%06ld.%06d %s::%s: _inLowPower %u\n"
- "%06ld.%06d %s::%s: _mapper %p\n"
- "%06ld.%06d %s::%s: _mediaInterfaceCount = %u\n"
- "%06ld.%06d %s::%s: _mediaInterfaceMaxPendingWriteBytes = %u\n"
- "%06ld.%06d %s::%s: _mediaInterfaceStart = %u\n"
- "%06ld.%06d %s::%s: _memoryAlloc %u\n"
- "%06ld.%06d %s::%s: _pciService: %p\n"
- "%06ld.%06d %s::%s: _pendLockPort %u\n"
- "%06ld.%06d %s::%s: _pendPortEnable %u\n"
- "%06ld.%06d %s::%s: _vmForce: 0x%llx\n"
- "%06ld.%06d %s::%s: _wiredCount: %u\n"
- "%06ld.%06d %s::%s: _workLoopControl was not set yet\n"
- "%06ld.%06d %s::%s: action %s\n"
- "%06ld.%06d %s::%s: async call failed with 0x%08x\n"
- "%06ld.%06d %s::%s: asyncMode 0x%08x\n"
- "%06ld.%06d %s::%s: attempts %d\n"
- "%06ld.%06d %s::%s: bad refCon %p, _pciPublishNotifier %p, _pciTerminateNotifier %p\n"
- "%06ld.%06d %s::%s: bar0 %p\n"
- "%06ld.%06d %s::%s: baseband chipset unknown, using default\n"
- "%06ld.%06d %s::%s: baseband service is %s\n"
- "%06ld.%06d %s::%s: bearer ID : %u, switched to default data service!\n"
- "%06ld.%06d %s::%s: bearer ID : %u, switched to low latency data service!\n"
- "%06ld.%06d %s::%s: bearer ID: %u, enable: %u, serviceID: %u\n"
- "%06ld.%06d %s::%s: bearerID: %u, interfaceID: %u, enable: %u, ipAppenderSvc: %u\n"
- "%06ld.%06d %s::%s: blockForCommand %u\n"
- "%06ld.%06d %s::%s: bootStage %u\n"
- "%06ld.%06d %s::%s: buff %p, size %u\n"
- "%06ld.%06d %s::%s: buff %p, size %u, info 0x%llx\n"
- "%06ld.%06d %s::%s: buff 0x%llx, size %llu, completion %p\n"
- "%06ld.%06d %s::%s: buff 0x%llx, size %llu, flush %d, completion %p\n"
- "%06ld.%06d %s::%s: buff 0x%llx, size %u, completion %p\n"
- "%06ld.%06d %s::%s: buffer allocation of %uB failed\n"
- "%06ld.%06d %s::%s: calling _provider->close()\n"
- "%06ld.%06d %s::%s: can't allocate map\n"
- "%06ld.%06d %s::%s: cf %p, arg0 %p, arg1 %p\n"
- "%06ld.%06d %s::%s: cf %p, intervalUs %llu, arg0 %p, arg1 %p\n"
- "%06ld.%06d %s::%s: checking link speed, expect %u\n"
- "%06ld.%06d %s::%s: cmdSize %llu\n"
- "%06ld.%06d %s::%s: cmdSize %llu, policyInfo %p\n"
- "%06ld.%06d %s::%s: command %p\n"
- "%06ld.%06d %s::%s: command packets exhausted\n"
- "%06ld.%06d %s::%s: command: %p\n"
- "%06ld.%06d %s::%s: count (%u) > gaurantee (%u) + speculative (%u) counts\n "
- "%06ld.%06d %s::%s: count: %u\n"
- "%06ld.%06d %s::%s: count: %u, dequeued: %u\n"
- "%06ld.%06d %s::%s: creating dedicated queue set, index: %u\n"
- "%06ld.%06d %s::%s: creating default queue set, index: %u\n"
- "%06ld.%06d %s::%s: current asyncMode 0x%08x\n"
- "%06ld.%06d %s::%s: current state: %s\n"
- "%06ld.%06d %s::%s: dealloc packet %p directly\n"
- "%06ld.%06d %s::%s: dedicated queue set [ %u ]: %u\n"
- "%06ld.%06d %s::%s: default queue set [ %u ]: %u\n"
- "%06ld.%06d %s::%s: default queue set config is NULL!\n"
- "%06ld.%06d %s::%s: device %p, powerStateOrdinal %lu\n"
- "%06ld.%06d %s::%s: device %p, stateNumber %lu\n"
- "%06ld.%06d %s::%s: device descriptor name: %s\n"
- "%06ld.%06d %s::%s: device name: %s, pcie reset sep workaround needed: %d\n"
- "%06ld.%06d %s::%s: dir: %u\n"
- "%06ld.%06d %s::%s: direction %s, completion %p\n"
- "%06ld.%06d %s::%s: domain %u\n"
- "%06ld.%06d %s::%s: domain: %u, buff 0x%llx, size %llu, completion %p\n"
- "%06ld.%06d %s::%s: domainState: 0x%lx\n"
- "%06ld.%06d %s::%s: enable %u\n"
- "%06ld.%06d %s::%s: enable %u, failureFatal %u, enabled state: %u\n"
- "%06ld.%06d %s::%s: enable AER notification\n"
- "%06ld.%06d %s::%s: enable interrupt %u\n"
- "%06ld.%06d %s::%s: enable sleep %u\n"
- "%06ld.%06d %s::%s: enable: %u\n"
- "%06ld.%06d %s::%s: enablePCIPowerManagement failed 0x%x\n"
- "%06ld.%06d %s::%s: enabled %u, status 0x%08x\n"
- "%06ld.%06d %s::%s: enabled %u, status 0x%x\n"
- "%06ld.%06d %s::%s: enabled: %u, shouldEnable: %u\n"
- "%06ld.%06d %s::%s: enabling L1SS\n"
- "%06ld.%06d %s::%s: endpoint L1PMSS capability not found\n"
- "%06ld.%06d %s::%s: endpoint port PCIe capability not found\n"
- "%06ld.%06d %s::%s: error type %u, arg0 %p, arg1 %p\n"
- "%06ld.%06d %s::%s: failed bytes %llu, size %llu\n"
- "%06ld.%06d %s::%s: failed client is not attached\n"
- "%06ld.%06d %s::%s: failed err %d\n"
- "%06ld.%06d %s::%s: failed to add AER event source\n"
- "%06ld.%06d %s::%s: failed to add Rx submission queue event source workLoop: 0x%x\n"
- "%06ld.%06d %s::%s: failed to add interrupt source\n"
- "%06ld.%06d %s::%s: failed to add matching notification - Default\n"
- "%06ld.%06d %s::%s: failed to add node\n"
- "%06ld.%06d %s::%s: failed to allocate MessageQueue\n"
- "%06ld.%06d %s::%s: failed to allocate Queues\n"
- "%06ld.%06d %s::%s: failed to allocate _lock\n"
- "%06ld.%06d %s::%s: failed to allocate _pciServiceLock\n"
- "%06ld.%06d %s::%s: failed to allocate _rdQueueLock\n"
- "%06ld.%06d %s::%s: failed to allocate commandGate\n"
- "%06ld.%06d %s::%s: failed to allocate io command\n"
- "%06ld.%06d %s::%s: failed to allocate link speed timer\n"
- "%06ld.%06d %s::%s: failed to allocate memory\n"
- "%06ld.%06d %s::%s: failed to allocate timer\n"
- "%06ld.%06d %s::%s: failed to allocate workloop\n"
- "%06ld.%06d %s::%s: failed to allocatePrepareMemory 0x%x\n"
- "%06ld.%06d %s::%s: failed to calculate pool capacity\n"
- "%06ld.%06d %s::%s: failed to create AER event source\n"
- "%06ld.%06d %s::%s: failed to create AppleBasebandPCIIOCommand node\n"
- "%06ld.%06d %s::%s: failed to create AppleBasebandPCIMemoryCommand node\n"
- "%06ld.%06d %s::%s: failed to create AppleBasebandPCIMemoryPolicy node\n"
- "%06ld.%06d %s::%s: failed to create AppleBasebandPCIRequest node\n"
- "%06ld.%06d %s::%s: failed to create DMA command\n"
- "%06ld.%06d %s::%s: failed to create MessageQueue\n"
- "%06ld.%06d %s::%s: failed to create Rx Completion queue!\n"
- "%06ld.%06d %s::%s: failed to create Rx Submission queue!\n"
- "%06ld.%06d %s::%s: failed to create Rx pool\n"
- "%06ld.%06d %s::%s: failed to create Rx queue\n"
- "%06ld.%06d %s::%s: failed to create Rx submission queue\n"
- "%06ld.%06d %s::%s: failed to create Tx Completion queue!\n"
- "%06ld.%06d %s::%s: failed to create Tx Submission queue!\n"
- "%06ld.%06d %s::%s: failed to create Tx completion queue\n"
- "%06ld.%06d %s::%s: failed to create Tx pool\n"
- "%06ld.%06d %s::%s: failed to create Tx queue\n"
- "%06ld.%06d %s::%s: failed to create command gate\n"
- "%06ld.%06d %s::%s: failed to create event source at %u\n"
- "%06ld.%06d %s::%s: failed to create interrupt event source\n"
- "%06ld.%06d %s::%s: failed to create lock\n"
- "%06ld.%06d %s::%s: failed to create memory descriptor\n"
- "%06ld.%06d %s::%s: failed to create memory policy info\n"
- "%06ld.%06d %s::%s: failed to create pci service notifiers\n"
- "%06ld.%06d %s::%s: failed to create pool\n"
- "%06ld.%06d %s::%s: failed to create registration entry\n"
- "%06ld.%06d %s::%s: failed to get link speed: 0x%08x\n"
- "%06ld.%06d %s::%s: failed to get mapper\n"
- "%06ld.%06d %s::%s: failed to get provider of IOPCI2PCIBridge\n"
- "%06ld.%06d %s::%s: failed to get provider of IOPCIDevice\n"
- "%06ld.%06d %s::%s: failed to get work loop\n"
- "%06ld.%06d %s::%s: failed to initialize Rx submission queue: 0x%x\n"
- "%06ld.%06d %s::%s: failed to map bar0\n"
- "%06ld.%06d %s::%s: failed to map bar1\n"
- "%06ld.%06d %s::%s: failed to map bar2\n"
- "%06ld.%06d %s::%s: failed to map memory for %p\n"
- "%06ld.%06d %s::%s: failed to open service\n"
- "%06ld.%06d %s::%s: failed to prepare 0x%x\n"
- "%06ld.%06d %s::%s: failed to prepare Rx pool, 0x%x\n"
- "%06ld.%06d %s::%s: failed to prepare Tx pool, 0x%x\n"
- "%06ld.%06d %s::%s: failed to prepare dma memory for %p\n"
- "%06ld.%06d %s::%s: failed to prepare io command\n"
- "%06ld.%06d %s::%s: failed to prepare log buffer\n"
- "%06ld.%06d %s::%s: failed to prepare qctun Rx buffer pool, 0x%x\n"
- "%06ld.%06d %s::%s: failed to prepare qctun Tx buffer pool, 0x%x\n"
- "%06ld.%06d %s::%s: failed to queue log buffer\n"
- "%06ld.%06d %s::%s: failed to read back bytes %llu, expected size %u\n"
- "%06ld.%06d %s::%s: failed to register network interface: 0x%x\n"
- "%06ld.%06d %s::%s: failed to retrieve DMA segment: 0x%x\n"
- "%06ld.%06d %s::%s: failed to retrieve any of the constants from plist\n"
- "%06ld.%06d %s::%s: failed to retrieve baseband chipset information\n"
- "%06ld.%06d %s::%s: failed to retrieve chipset device map\n"
- "%06ld.%06d %s::%s: failed to retrieve chipset name\n"
- "%06ld.%06d %s::%s: failed to retrieve dart window: 0x%x\n"
- "%06ld.%06d %s::%s: failed to retrieve device descriptor\n"
- "%06ld.%06d %s::%s: failed to retrieve device descriptor map\n"
- "%06ld.%06d %s::%s: failed to retrieve device descriptor name\n"
- "%06ld.%06d %s::%s: failed to retrieve pcie reset seperation workaround dict\n"
- "%06ld.%06d %s::%s: failed to retrieve workaround value\n"
- "%06ld.%06d %s::%s: failed to save registration entry\n"
- "%06ld.%06d %s::%s: failed to set link speed: 0x%08x\n"
- "%06ld.%06d %s::%s: failed to setup baseband service\n"
- "%06ld.%06d %s::%s: failed to setup control %p\n"
- "%06ld.%06d %s::%s: failed to setup port control %p\n"
- "%06ld.%06d %s::%s: failed to start reporting\n"
- "%06ld.%06d %s::%s: failed: 0x%x\n"
- "%06ld.%06d %s::%s: faled to copy data out of mbuf\n"
- "%06ld.%06d %s::%s: flags 0x%x, current state: %s\n"
- "%06ld.%06d %s::%s: flush %u\n"
- "%06ld.%06d %s::%s: forClient %p\n"
- "%06ld.%06d %s::%s: forClient %p, options 0x%08x, inGate %u\n"
- "%06ld.%06d %s::%s: forClient is not AppleBasebandPCIPDPSkywalkInterface\n"
- "%06ld.%06d %s::%s: force: %u, inReset = %u\n"
- "%06ld.%06d %s::%s: free count: %u\n"
- "%06ld.%06d %s::%s: got kOffPowerState\n"
- "%06ld.%06d %s::%s: got kOnPowerState\n"
- "%06ld.%06d %s::%s: got pci publish notifier\n"
- "%06ld.%06d %s::%s: got pci termination notifier\n"
- "%06ld.%06d %s::%s: got publish notifier\n"
- "%06ld.%06d %s::%s: got termination notifier\n"
- "%06ld.%06d %s::%s: ifnet_eflags not in plist\n"
- "%06ld.%06d %s::%s: ifp 0x%p, cmd 0x%x, data 0x%p\n"
- "%06ld.%06d %s::%s: ignore event %d\n"
- "%06ld.%06d %s::%s: ignoring transition\n"
- "%06ld.%06d %s::%s: in-band assert %u\n"
- "%06ld.%06d %s::%s: inReset %u\n"
- "%06ld.%06d %s::%s: index %d\n"
- "%06ld.%06d %s::%s: index %d, getInterruptType error 0x%08x\n"
- "%06ld.%06d %s::%s: index %d, not msi %d\n"
- "%06ld.%06d %s::%s: index %u\n"
- "%06ld.%06d %s::%s: index out of range %d\n"
- "%06ld.%06d %s::%s: interface %u %s\n"
- "%06ld.%06d %s::%s: interface down\n"
- "%06ld.%06d %s::%s: interface was not able to deallocate packet, force deallocating\n"
- "%06ld.%06d %s::%s: interfaces not available\n"
- "%06ld.%06d %s::%s: interval in us %llu, time mode %u\n"
- "%06ld.%06d %s::%s: intfPropMatches %u\n"
- "%06ld.%06d %s::%s: invalid descriptor\n"
- "%06ld.%06d %s::%s: invalid device\n"
- "%06ld.%06d %s::%s: invalid max_rsc_pkts config\n"
- "%06ld.%06d %s::%s: invalid max_rx_aggregation config\n"
- "%06ld.%06d %s::%s: invalid memory %p+%llu\n"
- "%06ld.%06d %s::%s: invalid message %u\n"
- "%06ld.%06d %s::%s: invalid param\n"
- "%06ld.%06d %s::%s: invalid plist, constants not dictionary\n"
- "%06ld.%06d %s::%s: invalid range: 0x%llx (+ 0x%llx)\n"
- "%06ld.%06d %s::%s: io: %p, iocmd: %p, status 0x%x, size %u, eot %d\n"
- "%06ld.%06d %s::%s: iocmd: %p, prev: %p, io: %p, pa: 0x%llx, OOO IO: %u, Intf Idx: %u, Chan Idx: %u, id: %u\n"
- "%06ld.%06d %s::%s: isDefaultQueueSet: %u\n"
- "%06ld.%06d %s::%s: link control2: 0x%08x, current target link speed: %u\n"
- "%06ld.%06d %s::%s: link control2: 0x%08x, target link speed: %u\n"
- "%06ld.%06d %s::%s: link speed mismatch: expected %u, actual %u\n"
- "%06ld.%06d %s::%s: linkState %u\n"
- "%06ld.%06d %s::%s: logical link / interface down\n"
- "%06ld.%06d %s::%s: logical link property is NULL!\n"
- "%06ld.%06d %s::%s: map %u\n"
- "%06ld.%06d %s::%s: mapped bar0 address 0x%llx (pa: 0x%llx) (+0x%x)\n"
- "%06ld.%06d %s::%s: mapped bar1 address 0x%llx (pa: 0x%llx) (+0x%x)\n"
- "%06ld.%06d %s::%s: mapped bar2 address 0x%llx (pa: 0x%llx) (+0x%x)\n"
- "%06ld.%06d %s::%s: mapper %p\n"
- "%06ld.%06d %s::%s: mapper 0x%p\n"
- "%06ld.%06d %s::%s: mapper cleared\n"
- "%06ld.%06d %s::%s: mapping bearer ID: %u, to queueset failed!\n"
- "%06ld.%06d %s::%s: mapping pending segments\n"
- "%06ld.%06d %s::%s: mbuf allocate failed err %d\n"
- "%06ld.%06d %s::%s: mem: %p\n"
- "%06ld.%06d %s::%s: memory limit reached\n"
- "%06ld.%06d %s::%s: memory not dart page aligned 0x%llx\n"
- "%06ld.%06d %s::%s: memory size not multiple of dart page size %llu\n"
- "%06ld.%06d %s::%s: memoryAllocLimit %llu, mapper %p\n"
- "%06ld.%06d %s::%s: messaging clients: message %s (0x%x), arg %p\n"
- "%06ld.%06d %s::%s: mmio read fail at %p\n"
- "%06ld.%06d %s::%s: muxed rx slot count not found in plist\n"
- "%06ld.%06d %s::%s: name: %s"
- "%06ld.%06d %s::%s: no manager\n"
- "%06ld.%06d %s::%s: no mapper\n"
- "%06ld.%06d %s::%s: no memory\n"
- "%06ld.%06d %s::%s: no pci service\n"
- "%06ld.%06d %s::%s: no provider\n"
- "%06ld.%06d %s::%s: no registration for time domain %u\n"
- "%06ld.%06d %s::%s: no slot available\n"
- "%06ld.%06d %s::%s: nomem\n"
- "%06ld.%06d %s::%s: nonmem for interface array\n"
- "%06ld.%06d %s::%s: not an AppleBasebandPCIPDPSkywalkInterface\n"
- "%06ld.%06d %s::%s: not disabling a device in reset\n"
- "%06ld.%06d %s::%s: not in sleep, bail\n"
- "%06ld.%06d %s::%s: nothing to process\n"
- "%06ld.%06d %s::%s: notifying AppleBaseband that PCI driver is registered for notifications\n"
- "%06ld.%06d %s::%s: oob Tx info allocation\n"
- "%06ld.%06d %s::%s: open failed, _pciService: %p\n"
- "%06ld.%06d %s::%s: options 0x%08x\n"
- "%06ld.%06d %s::%s: owner %u\n"
- "%06ld.%06d %s::%s: owner: %p, bearer ID: %u, status: %u\n"
- "%06ld.%06d %s::%s: packet %p\n"
- "%06ld.%06d %s::%s: packet allocation failed: 0x%x\n"
- "%06ld.%06d %s::%s: packet return %p\n"
- "%06ld.%06d %s::%s: pci bridge - device %p, stateNumber %lu\n"
- "%06ld.%06d %s::%s: pci bridge -- power on\n"
- "%06ld.%06d %s::%s: pci control, stateNumber %lu\n"
- "%06ld.%06d %s::%s: pci device open ret %u\n"
- "%06ld.%06d %s::%s: pci low power entry ack timeout\n"
- "%06ld.%06d %s::%s: pci low power entry acknowledged\n"
- "%06ld.%06d %s::%s: pci low power entry deferred\n"
- "%06ld.%06d %s::%s: pci service - device %p, stateNumber %lu\n"
- "%06ld.%06d %s::%s: pci service ID: %u\n"
- "%06ld.%06d %s::%s: pci service entered low power\n"
- "%06ld.%06d %s::%s: pci service exited low power\n"
- "%06ld.%06d %s::%s: pci service missing or in low power\n"
- "%06ld.%06d %s::%s: pci service not available\n"
- "%06ld.%06d %s::%s: pci service not available for MSI registration\n"
- "%06ld.%06d %s::%s: pci service open failed, service ID: %p\n"
- "%06ld.%06d %s::%s: pci service open failed, service: %p\n"
- "%06ld.%06d %s::%s: pci service: %p, isPublished: %u\n"
- "%06ld.%06d %s::%s: pciService not available\n"
- "%06ld.%06d %s::%s: pending\n"
- "%06ld.%06d %s::%s: plist does not contain constants for fallback (\"%s\")\n"
- "%06ld.%06d %s::%s: plist doesn't have Rx throughput specification\n"
- "%06ld.%06d %s::%s: plist doesn't have rx slot size\n"
- "%06ld.%06d %s::%s: plist doesn't have tx slot size\n"
- "%06ld.%06d %s::%s: plist error, constants property is not dictionary\n"
- "%06ld.%06d %s::%s: pool capacity: tx=%u, rx=%u\n"
- "%06ld.%06d %s::%s: pool not available\n"
- "%06ld.%06d %s::%s: pool: %p, Intf idx: %u\n"
- "%06ld.%06d %s::%s: port %p\n"
- "%06ld.%06d %s::%s: port already disabled\n"
- "%06ld.%06d %s::%s: port enable failed\n"
- "%06ld.%06d %s::%s: port enable failed!, ret: 0x%08x\n"
- "%06ld.%06d %s::%s: port enable panic setting: %u\n"
- "%06ld.%06d %s::%s: port is locked\n"
- "%06ld.%06d %s::%s: provider %p, options 0x%08x\n"
- "%06ld.%06d %s::%s: provider %p, options 0x%08x, defer %p\n"
- "%06ld.%06d %s::%s: provider is NULL\n"
- "%06ld.%06d %s::%s: provider is not AppleBasebandPCIPDPManagerBase\n"
- "%06ld.%06d %s::%s: provider is not an instance of AppleBasebandPCIInterface\n"
- "%06ld.%06d %s::%s: publishing %u PDP interfaces\n"
- "%06ld.%06d %s::%s: qctun interface enabled\n"
- "%06ld.%06d %s::%s: qctun interface number: %u\n"
- "%06ld.%06d %s::%s: qctun interface rx slot count not specified in plist!\n "
- "%06ld.%06d %s::%s: qctun interface rx slot count: %u\n"
- "%06ld.%06d %s::%s: qctun interface slot size not specified in plist!\n "
- "%06ld.%06d %s::%s: qctun interface slot size: %u\n"
- "%06ld.%06d %s::%s: qctun interface tx slot count not specified in plist!\n "
- "%06ld.%06d %s::%s: queue set config is NULL!\n"
- "%06ld.%06d %s::%s: queueSetID: 0x%llx, _isDefault: %u, index: %u\n"
- "%06ld.%06d %s::%s: raw Tx cached pkts: %u\n"
- "%06ld.%06d %s::%s: raw Tx freed pkts: %u\n"
- "%06ld.%06d %s::%s: refCon %p, _pciPublishNotifier %p, _pciTerminateNotifier %p\n"
- "%06ld.%06d %s::%s: refcon: %p, pci service: %p\n"
- "%06ld.%06d %s::%s: reg %d, size %d\n"
- "%06ld.%06d %s::%s: reg %u, buff %p, size %u\n"
- "%06ld.%06d %s::%s: region %u already mapped\n"
- "%06ld.%06d %s::%s: region %u not mapped\n"
- "%06ld.%06d %s::%s: region ID: %u, memory: %p, memorySize: %llu\n"
- "%06ld.%06d %s::%s: region Id: %u\n"
- "%06ld.%06d %s::%s: registered %p and set level to %u\n"
- "%06ld.%06d %s::%s: requested: %u, queued: %u\n"
- "%06ld.%06d %s::%s: requesting power state to be OFF\n"
- "%06ld.%06d %s::%s: requesting power state to be ON\n"
- "%06ld.%06d %s::%s: ret 0x%x, info 0x%llx\n"
- "%06ld.%06d %s::%s: retry %d\n"
- "%06ld.%06d %s::%s: root port L1PMSS capability not found\n"
- "%06ld.%06d %s::%s: root port PCIe capability not found\n"
- "%06ld.%06d %s::%s: rsc_service not present in plist or unsupported\n"
- "%06ld.%06d %s::%s: runAction failed with 0x%08x\n"
- "%06ld.%06d %s::%s: runAsync failed: %s\n"
- "%06ld.%06d %s::%s: rx pool capacity count not found in plist\n"
- "%06ld.%06d %s::%s: rx pool unavailable\n"
- "%06ld.%06d %s::%s: same mapper, skip remapping\n"
- "%06ld.%06d %s::%s: segment %p\n"
- "%06ld.%06d %s::%s: served %u raw Tx, %u remain\n"
- "%06ld.%06d %s::%s: service %p is not AppleBasebandPCI object\n"
- "%06ld.%06d %s::%s: service ID: %u\n"
- "%06ld.%06d %s::%s: service already open by %p\n"
- "%06ld.%06d %s::%s: service is terminating\n"
- "%06ld.%06d %s::%s: serviceID: %u, not present\n"
- "%06ld.%06d %s::%s: serviceID: %u, serviceObj: %p published\n"
- "%06ld.%06d %s::%s: set link speed to %u\n"
- "%06ld.%06d %s::%s: set power request %d\n"
- "%06ld.%06d %s::%s: shared mem unmapping failed: 0x%x\n"
- "%06ld.%06d %s::%s: shared memory mapping for region: %u, failed\n"
- "%06ld.%06d %s::%s: signal output request\n"
- "%06ld.%06d %s::%s: size %llu\n"
- "%06ld.%06d %s::%s: skipping port enable due to system power (sleep %d, shutdown %d)\n"
- "%06ld.%06d %s::%s: staged: %u\n"
- "%06ld.%06d %s::%s: success\n"
- "%06ld.%06d %s::%s: super class failed to initialize\n"
- "%06ld.%06d %s::%s: super failed\n"
- "%06ld.%06d %s::%s: super match failed\n"
- "%06ld.%06d %s::%s: super returned false\n"
- "%06ld.%06d %s::%s: super::init failed\n"
- "%06ld.%06d %s::%s: super::start failed\n"
- "%06ld.%06d %s::%s: t %u, arg0 %p, arg1 %p\n"
- "%06ld.%06d %s::%s: this %p\n"
- "%06ld.%06d %s::%s: this %p, pool %p, memPolicy %p\n"
- "%06ld.%06d %s::%s: this %p, status 0x%x, size %llu, cookie %p\n"
- "%06ld.%06d %s::%s: this: %p\n"
- "%06ld.%06d %s::%s: thread call failed with 0x%08x\n"
- "%06ld.%06d %s::%s: time event for domain %u is already registered\n"
- "%06ld.%06d %s::%s: timerMode %u, arg1 %p\n"
- "%06ld.%06d %s::%s: trigger power state change\n"
- "%06ld.%06d %s::%s: tx pool unavailable\n"
- "%06ld.%06d %s::%s: type %d status 0x%x header 0x%x 0x%x 0x%x 0x%x\n"
- "%06ld.%06d %s::%s: unRegistering MSI for index %u\n"
- "%06ld.%06d %s::%s: unable to allocate link status report staging buffer\n"
- "%06ld.%06d %s::%s: unable to configure the IPAppender for ifnet\n"
- "%06ld.%06d %s::%s: unable to create PCIfoundAB dictionary\n"
- "%06ld.%06d %s::%s: unable to create link speed dictionary\n"
- "%06ld.%06d %s::%s: unable to create matching dictionary\n"
- "%06ld.%06d %s::%s: unable to create port enable dictionaries\n"
- "%06ld.%06d %s::%s: unable to create port sleep enable/disable dictionaries\n"
- "%06ld.%06d %s::%s: unable to find AppleBasebandPCIPDPManagerBase service\n"
- "%06ld.%06d %s::%s: unable to find AppleIPAppender service\n"
- "%06ld.%06d %s::%s: unable to initialize pending segment list\n"
- "%06ld.%06d %s::%s: unable to unmap memory segment.\n"
- "%06ld.%06d %s::%s: unit number %u already has a session open\n"
- "%06ld.%06d %s::%s: unit number %u invalid or nonexistent\n"
- "%06ld.%06d %s::%s: unknown baseband chipset %s, no fallback option\n"
- "%06ld.%06d %s::%s: unknown client\n"
- "%06ld.%06d %s::%s: unknown message 0x%x\n"
- "%06ld.%06d %s::%s: unmapped bar\n"
- "%06ld.%06d %s::%s: unmapping leftover region %u\n"
- "%06ld.%06d %s::%s: va 0x%llx, pa 0x%llx, offset %llu\n"
- "%06ld.%06d %s::%s: vendorID = 0x%04x, deviceID = 0x%04x\n"
- "%06ld.%06d %s::%s: wait %u, event %p\n"
- "%06ld.%06d %s::%s: workloop: %p\n"
- "%3u"
- "%3u to %3u"
- "%3u to inf"
- "%d. size %llu, %p "
- "%s Close"
- "%s Open "
- "%s Read "
- "%s TimeSync"
- "%s Write"
- "%s: %u:%u was not found\n"
- "%s: logger user knob %u:%u already registered\n"
- "+-----------------------------------------------+----------------+"
- "/Library/Caches/com.apple.xbs/Sources/AppleBasebandPCI/AppleBasebandPCIControl/AppleBasebandPCILogger.cpp"
- "/Library/Caches/com.apple.xbs/Sources/AppleBasebandPCI/AppleBasebandPCIPDP/AppleBasebandPCIPDPReporter.cpp"
- "11211"
- "112111111"
- "1211"
- "1211111212221212111111112111112111111111111112112112112111121121111121"
- "12111112122212121111111121111121111111111111121121121121111211211111212"
- "121111121222121211112111222222212111112222212121"
- "121111121222121212111111111111111111111122122122221111111111222"
- "12111112122212121212111111111111111111111122222222222222222222222222222222222111111111111111111111111111111111111111111111111111111111111111111111122222222222222222111112112222222"
- "12111112122212121222222222111222112111112"
- "12112221111111111111"
- "12212"
- "Advanced Error Reporting"
- "Aggregated Block"
- "AppleBasebandPCI state dump:\n"
- "AppleBasebandPCI::start: failed to get logger\n"
- "AppleBasebandPCIControlReporter"
- "AppleBasebandPCILogger"
- "AppleBasebandPCILogger.cpp"
- "AppleBasebandPCILogger::initWithInfo: AppleBasebandPCILogger instance already exists\n"
- "AppleBasebandPCILogger::initWithInfo: pDictionary creation failed\n"
- "AppleBasebandPCILogger::initWithInfo: super::init failed\n"
- "AppleBasebandPCILogger::start: failed to allocate memory for snapshot buffer\n"
- "AppleBasebandPCIPDPManagerBase::start: failed to get logger\n"
- "AppleBasebandPCIPDPReporter"
- "AppleBasebandPCIPDPReporter.cpp"
- "AppleBasebandPCIReporter"
- "AppleBasebandPCIReporter::%s: could not create a legend\n"
- "AppleBasebandPCIReporter::%s: could not create a set object\n"
- "AppleBasebandPCIReporter::%s: invalid argument\n"
- "AppleBasebandPCIReporter::%s: setProperty failed\n"
- "AppleBasebandPCIReporter::%s: subclass failed to add reporters\n"
- "Binary"
- "Correctable Error"
- "Counters"
- "Current State Index"
- "DL"
- "DL Aggregation Histogram"
- "DL Drop Counters"
- "DL Limit"
- "DL Limiter State"
- "Downlink Bytes"
- "Downlink Pkts"
- "Dropped Downlink Bytes"
- "Dropped Downlink Packets"
- "Error"
- "False"
- "Fatal Error"
- "Flow Control"
- "Global"
- "I"
- "I/O"
- "IOReportLegend"
- "IOReportLegendPublic"
- "Interfaces"
- "Interrupt"
- "Invalid Interface"
- "Link Status Notifications"
- "Non-Fatal Error"
- "PDP"
- "PDP packet dump level"
- "PDP packet dump new level: %u\n"
- "PDP packet dump size"
- "Power"
- "Publish Count"
- "Secondary ISR Count"
- "Secondary Interrupt Handler"
- "State Summary"
- "States"
- "Terminate Count"
- "True"
- "UL"
- "UL Aggregation Histogram"
- "Uplink Bytes"
- "Uplink Pkts"
- "abortChannel"
- "abp-debug"
- "abp-debug-buf-size"
- "abp-flags"
- "abp-kdbg-trace"
- "abp-reporting"
- "addNode"
- "allocQueues"
- "allocatePrepareMemory"
- "allocateRawTxCache"
- "allocateReturnCommand"
- "asyncFunction"
- "asyncThreadCallGated"
- "bounceIn"
- "bounceOut"
- "calculateBufferPoolCapacity"
- "callAsync"
- "cancel"
- "cancelAsync"
- "cancelCompletion"
- "cancelTimer"
- "changeState"
- "checkPortAction"
- "checkPortOffCycleGated"
- "cleanCommandParamters"
- "cleanRequestParamters"
- "clearDMATransfer"
- "clientClose"
- "clientCloseGated"
- "close"
- "closeGated"
- "closePublishedPCIDataServicesGated"
- "closeServiceGated"
- "complete"
- "completeGatedFunction"
- "completeMemory"
- "configureReport"
- "createDedicatedQueueSet"
- "createDefaultQueueSet"
- "createInitRxSubmissionQueue"
- "createLogicalLinkGated_block_invoke"
- "createQueueSets"
- "createQueues"
- "createRxSubmissionQueue"
- "createSetupPort"
- "currentLogSnapshotBufferSize"
- "dartErrorHandler"
- "deRegisterPort"
- "deregisterTimeEvent"
- "deregisterUserKnob"
- "deviceAwakeCheck"
- "deviceWakeAsync"
- "deviceWakeFunction"
- "didTerminate"
- "disableLockPort"
- "disableLockPortGated"
- "discardRxPacket"
- "down"
- "enableASPMGated"
- "enableDefaultQueueSet"
- "enableHostMemProtectionGated"
- "enableL1SSGated"
- "enableUnlockPort"
- "enableUnlockPortGated"
- "enqueuePDPEvent"
- "enqueuePackets"
- "enterLowPower"
- "errorFunction"
- "exitLowPower"
- "failed to create logger\n"
- "flushQueueSets"
- "flushStageQueue"
- "free"
- "freeRawTxCache"
- "gatedReturnCommand"
- "gatherEPConfigRegSpace"
- "getChipsetConstants"
- "getCommand"
- "getCurrentLinkSpeedGated"
- "getDeviceDescriptorDict"
- "getDeviceResetState"
- "getEPTransactionPendingBit"
- "getInLowPower"
- "getInReset"
- "getQCTunBufferPool"
- "handleAER"
- "handleClose"
- "handleIsOpen"
- "handleOpen"
- "handlePCIMessage"
- "handlePCIServiceSwitch"
- "initBSDInterfaceParameters"
- "initUserDefaults"
- "initWithInfo"
- "initWithName"
- "initWithOptions"
- "initWithPool"
- "initWithWorkLoop"
- "initialPowerStateForDomainState"
- "initialize"
- "invokeAsync"
- "ioCompletionFunction"
- "ipAppenderMessage"
- "isPCIServicePublished"
- "linkDown"
- "linkDownCheck"
- "linkSpeedCheck"
- "linkStateUpFunction"
- "linkUp"
- "linkUpCheck"
- "lockPort"
- "logPacket"
- "logSnapshotBufferSize"
- "logger attach/start failed %p\n"
- "manualDisablePort"
- "manualEnablePort"
- "map"
- "mapBarGated"
- "mapBearerToQueueSet"
- "mapSharedMemory"
- "mapSharedMemory_block_invoke"
- "matchPropertyTable"
- "mmioRead"
- "mmioReadMemory"
- "msiInterrupt"
- "newMemorySegment"
- "newPacket"
- "notify"
- "notifyDedicatedBearer"
- "notifyPCIServiceDidTerminateGated"
- "notifyPCIServiceGated"
- "notifyPortStateChange"
- "notifyTerminateAck"
- "notifyTerminateAckGated"
- "open"
- "openGated"
- "openPublishedPCIDataServicesGated"
- "openServiceGated"
- "packetDump"
- "pciMessageGated"
- "pciNotifier"
- "pciRegisterGated"
- "pciServiceNotifyDidTerminate"
- "pciServiceNotifyDidTerminateGated"
- "pciServiceNotifyPublishGated"
- "pciServiceNotifyTerminateGated"
- "pcieResetSeperationROMWA"
- "pdp:%s: error %d\n"
- "pdp:%s: size (%u) out of range.\n"
- "pdpEventHandler"
- "pdp_dump_level"
- "pdp_dump_size"
- "pdp_ip%u"
- "portAction"
- "portActionDone"
- "portChangeFunction"
- "portDeepSleep"
- "portEnable"
- "portEnabled"
- "portManualEnableFunction"
- "portQuiesceWaitFunction"
- "portSleep"
- "portWake"
- "powerStateDidChangeTo"
- "powerStateDidChangeToGated"
- "powerStateWillChangeTo"
- "powerStateWillChangeToGated"
- "prepare"
- "prepareBSDInterface"
- "prepareDMATransfer"
- "prepareIn"
- "prepareMemory"
- "prepareOut"
- "preparePoolsWithMapper"
- "processBSDCommand"
- "processCurrentPortAction"
- "publish"
- "qctunBufferPoolCapacity"
- "queryFreeSpace"
- "queueLogBuffer"
- "queueRxBuffersGated"
- "rawTxPrepare"
- "read"
- "readLogs"
- "registerAER"
- "registerDARTErrorHandler"
- "registerDebugObject"
- "registerMSI"
- "registerMSI_block_invoke"
- "registerPort"
- "registerRead"
- "registerTimeEvent"
- "registerUserKnob"
- "registerWorkLoop"
- "releaseBasebandService"
- "reportError"
- "reportInterfaceAdvisory"
- "reportLinkStatus"
- "reportMessage"
- "requestDequeue"
- "requestPortOffCycleGated"
- "requestTxGated"
- "resetStageQueue"
- "returnPacket"
- "running"
- "rxQueueCallbackGated"
- "scan"
- "sendImage"
- "serveRawTxQueue"
- "serviceNotifier"
- "serviceRegisterGated"
- "setBootStage"
- "setIO"
- "setInReset"
- "setLinkSpeedGated"
- "setMapper"
- "setName"
- "setPowerOn"
- "setPowerState"
- "setPowerStateGated"
- "setQueueSetId"
- "setRunningState"
- "setTargetLinkSpeedGated"
- "setupBasebandService"
- "setupDARTWindowGated"
- "setupPort"
- "shared memory"
- "site.AppleBasebandPCIControlReporter"
- "site.AppleBasebandPCILogger"
- "site.AppleBasebandPCIPDPReporter"
- "site.AppleBasebandPCIReporter"
- "site.IOSimpleReporter*"
- "site.IOStateReporter*"
- "site.StateEntry"
- "site.UserKnob"
- "site.logBuffer"
- "site.logBufferQueue"
- "site.struct StateEntry"
- "sleepAckFunction"
- "sleepCheck"
- "some logs dropped\n"
- "stagePkts"
- "stageQueueGetRxPkts"
- "stageQueueGetTxPkts"
- "startChannel"
- "startReporting"
- "startSleepTimer"
- "startTimer"
- "stop"
- "stopped"
- "switchBearerTrafficToService"
- "syncSIOCSIFFLAGS"
- "sysctl_pdp_dump_level"
- "sysctl_pdp_dump_size"
- "teardownPort"
- "telescoperRecordCompletedPackets"
- "terminate"
- "timeSync"
- "timer"
- "timerCompletion"
- "timerFunction"
- "transferDone"
- "triggerMSI"
- "triggerTxDequeue"
- "txCompletionCallbackGated"
- "txQueueCallbackGated"
- "unRegisterMSI"
- "unRegisterMSI_block_invoke"
- "unlockPort"
- "unmap"
- "unmapBarGated"
- "unmapBearerFromQueueSet"
- "unmapSharedMemory"
- "unmapSharedMemory_block_invoke"
- "up"
- "updateEnabled"
- "updateReport"
- "usesLowLatencyService"
- "usesRSCService"
- "validateMSIIndex"
- "willTerminate"
- "willTerminateGated"
- "write"
- "|%02x %02x %02x %02x %02x %02x %02x %02x %02x %02x %02x %02x %02x %02x %02x %02x|%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c|"
- "~ABPControl"
- "~ABPNullDevice"
- "~ABPPort"

```

>  `com.apple.driver.AppleBasebandPCIMAVControl`

```diff

 810.0.0.0.0
   __TEXT.__const: 0x262a
-  __TEXT.__cstring: 0x67ee
-  __TEXT_EXEC.__text: 0x511fc
+  __TEXT.__cstring: 0x11c5
+  __TEXT_EXEC.__text: 0x283ac
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x140
-  __DATA.__common: 0x100
+  __DATA.__common: 0xd8
   __DATA.__bss: 0x1760
-  __DATA_CONST.__auth_got: 0x298
-  __DATA_CONST.__got: 0xd8
-  __DATA_CONST.__mod_init_func: 0xaf8
-  __DATA_CONST.__mod_term_func: 0x38
-  __DATA_CONST.__const: 0x7dc0
-  __DATA_CONST.__kalloc_type: 0xc80
+  __DATA_CONST.__auth_got: 0x258
+  __DATA_CONST.__got: 0xc8
+  __DATA_CONST.__mod_init_func: 0xaf0
+  __DATA_CONST.__mod_term_func: 0x30
+  __DATA_CONST.__const: 0x7c38
+  __DATA_CONST.__kalloc_type: 0xc40
   __DATA_CONST.__kalloc_var: 0x5a0
-  Functions: 1079
+  Functions: 1053
   Symbols:   0
-  CStrings:  720
+  CStrings:  177
 
CStrings:
+ "121111121222121212111111111111111111111122122122221111111112222"
- "%06ld.%06d %s::%s: \n"
- "%06ld.%06d %s::%s:  --done\n"
- "%06ld.%06d %s::%s: %d. \n"
- "%06ld.%06d %s::%s: %d.  --done\n"
- "%06ld.%06d %s::%s: %d. %p [0x%llx]\n"
- "%06ld.%06d %s::%s: %d. %p [0x%llx], queued IOs: %lu\n"
- "%06ld.%06d %s::%s: %d. %s -> %s\n"
- "%06ld.%06d %s::%s: %d. (async) failed to prepare memory command\n"
- "%06ld.%06d %s::%s: %d. (async) returned 0x%x\n"
- "%06ld.%06d %s::%s: %d. -- done\n"
- "%06ld.%06d %s::%s: %d. -- done %u\n"
- "%06ld.%06d %s::%s: %d. --done\n"
- "%06ld.%06d %s::%s: %d. Copy memory command\n"
- "%06ld.%06d %s::%s: %d. Device is IN RESET state, bailing\n"
- "%06ld.%06d %s::%s: %d. Exclusive workloop interface, failed to create a control commandGate!\n"
- "%06ld.%06d %s::%s: %d. Getting BB reset state failed\n"
- "%06ld.%06d %s::%s: %d. Unmap shared memory failed\n"
- "%06ld.%06d %s::%s: %d. Virtual timesync interface\n"
- "%06ld.%06d %s::%s: %d. _asyncMode 0x%08x, asyncMode 0x%08x, arg1 %p\n"
- "%06ld.%06d %s::%s: %d. asyncMode 0x%08x\n"
- "%06ld.%06d %s::%s: %d. buffer: 0x%llx, size: %llu, seqNum: %u\n"
- "%06ld.%06d %s::%s: %d. calling completion, ret: 0x%llx\n"
- "%06ld.%06d %s::%s: %d. cf %p, arg0 %p, arg1 %p\n"
- "%06ld.%06d %s::%s: %d. chunk too large\n"
- "%06ld.%06d %s::%s: %d. commandSleep (THREAD_INTERRUPTIBLE) woke with reason 0x%x\n"
- "%06ld.%06d %s::%s: %d. current asyncMode 0x%08x\n"
- "%06ld.%06d %s::%s: %d. direction %s\n"
- "%06ld.%06d %s::%s: %d. direction %u\n"
- "%06ld.%06d %s::%s: %d. direction: %u, workloop: %p\n"
- "%06ld.%06d %s::%s: %d. do not support no copy for mbuf\n"
- "%06ld.%06d %s::%s: %d. error %u\n"
- "%06ld.%06d %s::%s: %d. error type %u, arg0 %p, arg1 %p\n"
- "%06ld.%06d %s::%s: %d. eventIndex %u\n"
- "%06ld.%06d %s::%s: %d. exclusive workloop: %p, msi index: %u\n"
- "%06ld.%06d %s::%s: %d. failed to allocate async interrupt source\n"
- "%06ld.%06d %s::%s: %d. failed to allocate commandGate\n"
- "%06ld.%06d %s::%s: %d. failed to allocate io pool\n"
- "%06ld.%06d %s::%s: %d. failed to allocate memory\n"
- "%06ld.%06d %s::%s: %d. failed to allocate memory command\n"
- "%06ld.%06d %s::%s: %d. failed to create async call lock\n"
- "%06ld.%06d %s::%s: %d. failed to create pools\n"
- "%06ld.%06d %s::%s: %d. failed to prepare memory 0x%x\n"
- "%06ld.%06d %s::%s: %d. failed to prepare memory command\n"
- "%06ld.%06d %s::%s: %d. failed to register channel\n"
- "%06ld.%06d %s::%s: %d. failed to retrieve channel direction\n"
- "%06ld.%06d %s::%s: %d. failed to setup channel\n"
- "%06ld.%06d %s::%s: %d. failed to setup interface _outChannel %p, _inChannel %p\n"
- "%06ld.%06d %s::%s: %d. failed to setup transfer ring\n"
- "%06ld.%06d %s::%s: %d. forClient %p, options 0x%08x\n"
- "%06ld.%06d %s::%s: %d. forClient %p, options 0x%08x, arg %p\n"
- "%06ld.%06d %s::%s: %d. forClient %p, options 0x%08x, arg %p, inGate %u\n"
- "%06ld.%06d %s::%s: %d. forClient %p, options 0x%08x, inGate %u\n"
- "%06ld.%06d %s::%s: %d. incomplete io\n"
- "%06ld.%06d %s::%s: %d. index %u\n"
- "%06ld.%06d %s::%s: %d. interface is inactive\n"
- "%06ld.%06d %s::%s: %d. invalid channel direction\n"
- "%06ld.%06d %s::%s: %d. invalid channel protocol\n"
- "%06ld.%06d %s::%s: %d. invalid direction: %u for the interface\n"
- "%06ld.%06d %s::%s: %d. io %p, pa: 0x%llx, tre %p\n"
- "%06ld.%06d %s::%s: %d. io %p, size %u, pa 0x%llx\n"
- "%06ld.%06d %s::%s: %d. io %p, tre %p, io->_pa %p, cookie 0x%lx\n"
- "%06ld.%06d %s::%s: %d. io: %p, pa 0x%llx\n"
- "%06ld.%06d %s::%s: %d. io: %p, status 0x%x\n"
- "%06ld.%06d %s::%s: %d. io: %p, type: %u, status 0x%x, last: %u\n"
- "%06ld.%06d %s::%s: %d. malformed count, count: %u\n"
- "%06ld.%06d %s::%s: %d. map buffer ack failed: 0x%llx\n"
- "%06ld.%06d %s::%s: %d. map buffer ack timed out: 0x%llx\n"
- "%06ld.%06d %s::%s: %d. map completion failed\n"
- "%06ld.%06d %s::%s: %d. map completion failed, mem is NULL\n"
- "%06ld.%06d %s::%s: %d. map completion success\n"
- "%06ld.%06d %s::%s: %d. memCmd %p, size %llu\n"
- "%06ld.%06d %s::%s: %d. mem[%llu] %p, direction %u\n"
- "%06ld.%06d %s::%s: %d. mhiDevice %p\n"
- "%06ld.%06d %s::%s: %d. no in channel\n"
- "%06ld.%06d %s::%s: %d. no out channel\n"
- "%06ld.%06d %s::%s: %d. num of chunks in io too large\n"
- "%06ld.%06d %s::%s: %d. openGated failed, result: 0x%08x\n"
- "%06ld.%06d %s::%s: %d. options 0x%08x\n"
- "%06ld.%06d %s::%s: %d. pa 0x%llx, size %u, code %u\n"
- "%06ld.%06d %s::%s: %d. pa 0x%llx, size %u, code %u, ccid %u, queued IOs: %lu\n"
- "%06ld.%06d %s::%s: %d. packetChain %p\n"
- "%06ld.%06d %s::%s: %d. part1 subDescSize %llu, offset %llu\n"
- "%06ld.%06d %s::%s: %d. part1 subDesc[%llu] physical address 0x%llx\n"
- "%06ld.%06d %s::%s: %d. part2 subDescSize %llu, offset %llu\n"
- "%06ld.%06d %s::%s: %d. part2 subDesc[%llu] physical address 0x%llx\n"
- "%06ld.%06d %s::%s: %d. part3 subDescSize %llu, offset %llu\n"
- "%06ld.%06d %s::%s: %d. part3 subDesc[%llu] physical address 0x%llx\n"
- "%06ld.%06d %s::%s: %d. prop %p\n"
- "%06ld.%06d %s::%s: %d. provider %p, options 0x%08x\n"
- "%06ld.%06d %s::%s: %d. provider %p, options 0x%08x, defer %p\n"
- "%06ld.%06d %s::%s: %d. queued IOs: %u\n"
- "%06ld.%06d %s::%s: %d. reap elements\n"
- "%06ld.%06d %s::%s: %d. reliable %u\n"
- "%06ld.%06d %s::%s: %d. res = 0x%x, size = %llu, cookie %p\n"
- "%06ld.%06d %s::%s: %d. reset the channels\n"
- "%06ld.%06d %s::%s: %d. result: %u, seqNum: %u, bytes read: %u\n"
- "%06ld.%06d %s::%s: %d. ring - va: 0x%llx, pa: 0x%llx\\n"
- "%06ld.%06d %s::%s: %d. ring not aligned to %u\n"
- "%06ld.%06d %s::%s: %d. ring not large enough %u\n"
- "%06ld.%06d %s::%s: %d. ring va 0x%llx, pa 0x%llx, size %u\n"
- "%06ld.%06d %s::%s: %d. sending map message failed: 0x%llx\n"
- "%06ld.%06d %s::%s: %d. sending unmap message failed: 0x%llx\n"
- "%06ld.%06d %s::%s: %d. service is terminating\n"
- "%06ld.%06d %s::%s: %d. setting defaultInt %d, defaultIEOT %d, defaultIEOB %d\n"
- "%06ld.%06d %s::%s: %d. setting doorbellSetting time %llu, threshold %u\n"
- "%06ld.%06d %s::%s: %d. setting threshold intThreshold %d, ieotThreshold %d, ieobThreshold %d\n"
- "%06ld.%06d %s::%s: %d. setting up map message completion failed: 0x%llx\n"
- "%06ld.%06d %s::%s: %d. setting up unmap message completion failed: 0x%llx\n"
- "%06ld.%06d %s::%s: %d. sharedER %u\n"
- "%06ld.%06d %s::%s: %d. skipping channel setup for channel protocol: %s\n"
- "%06ld.%06d %s::%s: %d. status 0x%x\n"
- "%06ld.%06d %s::%s: %d. status: %u, size: %u\n"
- "%06ld.%06d %s::%s: %d. status: 0x%llx, size: %llu\n"
- "%06ld.%06d %s::%s: %d. super::start failed\n"
- "%06ld.%06d %s::%s: %d. sync %u\n"
- "%06ld.%06d %s::%s: %d. tre %p, size %u, code %u, last %u, io %p\n"
- "%06ld.%06d %s::%s: %d. trigger %u, index %u\n"
- "%06ld.%06d %s::%s: %d. type %u\n"
- "%06ld.%06d %s::%s: %d. type %u, completion code %u, asyncMode %u\n"
- "%06ld.%06d %s::%s: %d. unmap buffer ack timed out: 0x%llx\n"
- "%06ld.%06d %s::%s: %d. unmap completion failed\n"
- "%06ld.%06d %s::%s: %d. unmap completion failed, mem is NULL\n"
- "%06ld.%06d %s::%s: %d. unmap completion success\n"
- "%06ld.%06d %s::%s: %d. waiting for map completion\n"
- "%06ld.%06d %s::%s: %d. waiting for unmap completion\n"
- "%06ld.%06d %s::%s: %s -> %s\n"
- "%06ld.%06d %s::%s: %u\n"
- "%06ld.%06d %s::%s: (async) failed to create memory decriptor for shared memory region\n"
- "%06ld.%06d %s::%s: -- done\n"
- "%06ld.%06d %s::%s: -- done %u\n"
- "%06ld.%06d %s::%s: --done\n"
- "%06ld.%06d %s::%s: ABPDevice %p, type %u\n"
- "%06ld.%06d %s::%s: Bailing, device not alive\n!"
- "%06ld.%06d %s::%s: Both channels should have same msi_index values, (%u, %u)\n"
- "%06ld.%06d %s::%s: CHDBOFF (0x%x) invalid\n"
- "%06ld.%06d %s::%s: Could not find %s dictionary for time_sync!\n"
- "%06ld.%06d %s::%s: Could not find time_sync dictionary!\n"
- "%06ld.%06d %s::%s: Cur expiry: %llu\n"
- "%06ld.%06d %s::%s: Cur expiry: %llu < timeout: %llu\n"
- "%06ld.%06d %s::%s: Desired link speed: %u, boot stage: %u\n"
- "%06ld.%06d %s::%s: Device in Reset state! Skip sending unmap message!\n"
- "%06ld.%06d %s::%s: Device in low power, cannot immediately initiate time sync\n"
- "%06ld.%06d %s::%s: Device in low power, cannot initiate time sync\n"
- "%06ld.%06d %s::%s: ERDBOFF (0x%x) invalid\n"
- "%06ld.%06d %s::%s: ERE: res: 0x%lx, cookie: 0x%lx, code %u, ccid: %u, len: %u, allFields: 0x%lx\n"
- "%06ld.%06d %s::%s: Error 0x%x\n"
- "%06ld.%06d %s::%s: Error getting channel doorbell number for time_sync property!\n"
- "%06ld.%06d %s::%s: Event Ring Index %u: shared channel: %u\n"
- "%06ld.%06d %s::%s: Failed to allocate pending event queue for shared ER index: %u\n"
- "%06ld.%06d %s::%s: Failed to find time sync capability register\n"
- "%06ld.%06d %s::%s: Failed to get device properties dictionary\n"
- "%06ld.%06d %s::%s: Found time sync capability register\n"
- "%06ld.%06d %s::%s: Host sleep Deferred\n"
- "%06ld.%06d %s::%s: Inserting shared mem region with ID: %u\n"
- "%06ld.%06d %s::%s: Invalid domain: %u\n"
- "%06ld.%06d %s::%s: MHI Status: 0x%x\n"
- "%06ld.%06d %s::%s: MHI in error state! MHI Status: 0x%x\n"
- "%06ld.%06d %s::%s: MHI reset complete, MHICTRL: 0x%x\n"
- "%06ld.%06d %s::%s: MHI reset procedure failed!\n"
- "%06ld.%06d %s::%s: MSI registration failed, index: %u\n"
- "%06ld.%06d %s::%s: Map / Prepare shared memory failed: 0x%llx\n"
- "%06ld.%06d %s::%s: No MHI capability regiter found!\n"
- "%06ld.%06d %s::%s: No MHIChannel\n"
- "%06ld.%06d %s::%s: Registration for domain %u already exists\n"
- "%06ld.%06d %s::%s: Shared mem pa: 0x%llx, mem desc pa: %p\n"
- "%06ld.%06d %s::%s: Starting timer: New expiry: %llu, timeout: %llu\n"
- "%06ld.%06d %s::%s: Time capability addr: %p\n"
- "%06ld.%06d %s::%s: Time capability not present\n"
- "%06ld.%06d %s::%s: Time event call back registration is NULL\n"
- "%06ld.%06d %s::%s: Time sync completion unit: %u, time: %llu, domain: %u, seq: %u\n"
- "%06ld.%06d %s::%s: Time sync is not supported\n"
- "%06ld.%06d %s::%s: Time sync not supported\n"
- "%06ld.%06d %s::%s: Total shared ER count: %u\n"
- "%06ld.%06d %s::%s: Triggering MSI index: %u, failed ret: 0x%llx\n"
- "%06ld.%06d %s::%s: Unexpected Time sync completion unit, unit: %u\n"
- "%06ld.%06d %s::%s: Unmapping region Id: %u, buffer addr: %p\n"
- "%06ld.%06d %s::%s: Unsupported time domain for device wake assertion\n"
- "%06ld.%06d %s::%s: Using exclusive timer workloop\n"
- "%06ld.%06d %s::%s: _commandContext %p, _commandContextPa 0x%llx\n"
- "%06ld.%06d %s::%s: _commandRing va 0x%llx, pa 0x%llx, size %u\n"
- "%06ld.%06d %s::%s: _commandSetting._doorbellSetting time %llu, threshold %u\n"
- "%06ld.%06d %s::%s: _eventRing[%d] va 0x%llx, pa 0x%llx, size %u\n"
- "%06ld.%06d %s::%s: _eventSetting[%d] _intmod %d, _doorbellSetting time %llu, threshold %u, sync %u\n"
- "%06ld.%06d %s::%s: _mapBase 0x%llx, _mapLimit 0x%llx\n"
- "%06ld.%06d %s::%s: _msiRange[%d]: low %d, high %d\n"
- "%06ld.%06d %s::%s: _numChannelContext %u, _channelContext %p, _channelContextPa 0x%llx\n"
- "%06ld.%06d %s::%s: _numEventContext %u, _eventContext %p, _eventContextPa 0x%llx\n"
- "%06ld.%06d %s::%s: _numEvents %d\n"
- "%06ld.%06d %s::%s: _numHWEvents: %u, NUMHWER (from device): %d\n"
- "%06ld.%06d %s::%s: _numMSI %d\n"
- "%06ld.%06d %s::%s: _shadowChannelDoorbell[%u] 0x%llx\n"
- "%06ld.%06d %s::%s: _shadowCommandDoorbell 0x%llx\n"
- "%06ld.%06d %s::%s: _shadowEventDoorbell[%u] 0x%llx\n"
- "%06ld.%06d %s::%s: abort client io completion\n"
- "%06ld.%06d %s::%s: adjusted memSize %llu\n"
- "%06ld.%06d %s::%s: alignment %u\n"
- "%06ld.%06d %s::%s: allocate memory pool for %u\n"
- "%06ld.%06d %s::%s: applying device wake 0x%x\n"
- "%06ld.%06d %s::%s: assert %d, vote 0x%x, deviceWakeCurrent 0x%x _deviceWake 0x%x\n"
- "%06ld.%06d %s::%s: assert: %u, vote: 0x%08x\n"
- "%06ld.%06d %s::%s: bar0 0x%llx (+0x%x)\n"
- "%06ld.%06d %s::%s: bar1 0x%llx (+0x%x)\n"
- "%06ld.%06d %s::%s: bhi attach/start device failed %p\n"
- "%06ld.%06d %s::%s: bhi attach/start interface failed %p\n"
- "%06ld.%06d %s::%s: can't access device wake -- the doorbell is unavailable\n"
- "%06ld.%06d %s::%s: can't access device wake -- the link is not up\n"
- "%06ld.%06d %s::%s: capability count: %u, next cap: 0x%p\n"
- "%06ld.%06d %s::%s: cf %p, intervalUs %llu, arg0 %p, arg1 %p\n"
- "%06ld.%06d %s::%s: chID: %u, type: 0x%x, res2: 0x%x, allFlags: 0x%lx\n"
- "%06ld.%06d %s::%s: change M-state %d -> %d\n"
- "%06ld.%06d %s::%s: channel %u, instance %p, ring physical address 0x%llx\n"
- "%06ld.%06d %s::%s: channel count %d\n"
- "%06ld.%06d %s::%s: channelMemoryAllocInfo._pa 0x%llx\n"
- "%06ld.%06d %s::%s: channelMemoryAllocInfo._size %llu\n"
- "%06ld.%06d %s::%s: channelMemoryAllocInfo._va 0x%llx\n"
- "%06ld.%06d %s::%s: chipset_name: %s\n"
- "%06ld.%06d %s::%s: commandSleep (THREAD_INTERRUPTIBLE) woke with reason 0x%x\n"
- "%06ld.%06d %s::%s: control %p\n"
- "%06ld.%06d %s::%s: could not allocate _memoryPoolArray\n"
- "%06ld.%06d %s::%s: cre %p\n"
- "%06ld.%06d %s::%s: create %u, type %u\n"
- "%06ld.%06d %s::%s: direction invalid\n"
- "%06ld.%06d %s::%s: dmaCmd %p\n"
- "%06ld.%06d %s::%s: domain: %u, seq: %u, fullSeq: 0x%lx, mach continuous_begin: %llu\n"
- "%06ld.%06d %s::%s: done processing event rings\n"
- "%06ld.%06d %s::%s: duplicate send image\n"
- "%06ld.%06d %s::%s: error type %u, arg0 %p, arg1 %p\n"
- "%06ld.%06d %s::%s: event index out of range\n"
- "%06ld.%06d %s::%s: execution environment for current interfaces is %d. BB is changing to %d\n"
- "%06ld.%06d %s::%s: failed readBytes %llu, size %llu\n"
- "%06ld.%06d %s::%s: failed to alloc dma command\n"
- "%06ld.%06d %s::%s: failed to allocate _interface\n"
- "%06ld.%06d %s::%s: failed to allocate async call lock\n"
- "%06ld.%06d %s::%s: failed to allocate commandGate\n"
- "%06ld.%06d %s::%s: failed to allocate io pool\n"
- "%06ld.%06d %s::%s: failed to allocate lock\n"
- "%06ld.%06d %s::%s: failed to allocate memory\n"
- "%06ld.%06d %s::%s: failed to allocate memory for channels\n"
- "%06ld.%06d %s::%s: failed to allocate memory pool of size %d\n"
- "%06ld.%06d %s::%s: failed to allocate request pool\n"
- "%06ld.%06d %s::%s: failed to allocate resources for async completion\n"
- "%06ld.%06d %s::%s: failed to allocate timer\n"
- "%06ld.%06d %s::%s: failed to allocate timer commandGate\n"
- "%06ld.%06d %s::%s: failed to allocate timer workloop\n"
- "%06ld.%06d %s::%s: failed to allocate timesync event source\n"
- "%06ld.%06d %s::%s: failed to create bhi device\n"
- "%06ld.%06d %s::%s: failed to create bhi interface\n"
- "%06ld.%06d %s::%s: failed to create mhi device\n"
- "%06ld.%06d %s::%s: failed to create mhi interface\n"
- "%06ld.%06d %s::%s: failed to create pools\n"
- "%06ld.%06d %s::%s: failed to gen DMA address: 0x%x, numSeg %u, len %llu\n"
- "%06ld.%06d %s::%s: failed to get bhi offset\n"
- "%06ld.%06d %s::%s: failed to map memory in dart\n"
- "%06ld.%06d %s::%s: failed to map result buffer\n"
- "%06ld.%06d %s::%s: failed to prepare for DMA: 0x%x\n"
- "%06ld.%06d %s::%s: failed to prepare image 0x%x\n"
- "%06ld.%06d %s::%s: failed to prepare memory: 0x%x\n"
- "%06ld.%06d %s::%s: failed to read CHDBOFF\n"
- "%06ld.%06d %s::%s: failed to read ERDBOFF\n"
- "%06ld.%06d %s::%s: failed to read MHICFG\n"
- "%06ld.%06d %s::%s: failed to read MHISTATUS\n"
- "%06ld.%06d %s::%s: failed to read MHIVER\n"
- "%06ld.%06d %s::%s: failed to read capability register\n"
- "%06ld.%06d %s::%s: failed to read capability register offset\n"
- "%06ld.%06d %s::%s: failed to read execution environment\n"
- "%06ld.%06d %s::%s: failed to read getMHICTRL\n"
- "%06ld.%06d %s::%s: failed to read memory pool array object\n"
- "%06ld.%06d %s::%s: failed to setup channel %p\n"
- "%06ld.%06d %s::%s: failed to setup command ring\n"
- "%06ld.%06d %s::%s: failed to setup context\n"
- "%06ld.%06d %s::%s: failed to setup device\n"
- "%06ld.%06d %s::%s: failed to setup device %p\n"
- "%06ld.%06d %s::%s: failed to setup event ring\n"
- "%06ld.%06d %s::%s: forClient %p, options 0x%08x, inGate %u\n"
- "%06ld.%06d %s::%s: force: %u\n"
- "%06ld.%06d %s::%s: from %s -> %s\n"
- "%06ld.%06d %s::%s: fullSeq: 0x%lx\n"
- "%06ld.%06d %s::%s: got completion for deregistered channel %u\n"
- "%06ld.%06d %s::%s: hit %u, doorbell: %u\n"
- "%06ld.%06d %s::%s: ignore m1 entry\n"
- "%06ld.%06d %s::%s: imageSize = %llu\n"
- "%06ld.%06d %s::%s: image[%u] pa 0x%llx\n"
- "%06ld.%06d %s::%s: img %p\n"
- "%06ld.%06d %s::%s: in sleep, ignore\n"
- "%06ld.%06d %s::%s: incorrect alignment\n"
- "%06ld.%06d %s::%s: index %u\n"
- "%06ld.%06d %s::%s: index %u, ccid %u, cookie: 0x%lx, size %u, code %u, last %u\n"
- "%06ld.%06d %s::%s: index %u, command %u, seq %u, reliable %u\n"
- "%06ld.%06d %s::%s: index %u, ere %p, type %u\n"
- "%06ld.%06d %s::%s: index %u, pa 0x%llx, size %u, code %u\n"
- "%06ld.%06d %s::%s: index %u, write physical address 0x%llx\n"
- "%06ld.%06d %s::%s: index out of range\n"
- "%06ld.%06d %s::%s: initializing device wake to %s\n"
- "%06ld.%06d %s::%s: interface is inactive\n"
- "%06ld.%06d %s::%s: interval %llu\n"
- "%06ld.%06d %s::%s: interval in us %llu, time mode %u\n"
- "%06ld.%06d %s::%s: intfIdx %lu\n"
- "%06ld.%06d %s::%s: link state already up\n"
- "%06ld.%06d %s::%s: link state: %u, bailing!\n"
- "%06ld.%06d %s::%s: linkState %u\n"
- "%06ld.%06d %s::%s: looking for next cap at: 0x%p, offset (from bar0): %u\n"
- "%06ld.%06d %s::%s: memSize %llu\n"
- "%06ld.%06d %s::%s: memSize = %llu\n"
- "%06ld.%06d %s::%s: memory is not page aligned\n"
- "%06ld.%06d %s::%s: memory size is not page aligned\n"
- "%06ld.%06d %s::%s: mhi attach/start device failed %p\n"
- "%06ld.%06d %s::%s: mhi attach/start interface failed %p\n"
- "%06ld.%06d %s::%s: mhi state: %u\n"
- "%06ld.%06d %s::%s: msi in unexpected state %u\n"
- "%06ld.%06d %s::%s: msi index out of range\n"
- "%06ld.%06d %s::%s: msi index range overrun\n"
- "%06ld.%06d %s::%s: msi index: %u\n"
- "%06ld.%06d %s::%s: msi range malformed\n"
- "%06ld.%06d %s::%s: nothing to do here... bailing.\n"
- "%06ld.%06d %s::%s: numChannelContext (%u) greater than supported by device %d\n"
- "%06ld.%06d %s::%s: numEvents (%u) greater than supported by device %d\n"
- "%06ld.%06d %s::%s: numHWChannelContext (%u) greater than supported by device %d\n"
- "%06ld.%06d %s::%s: numHWEvents (%u) greater than supported by device %d\n"
- "%06ld.%06d %s::%s: options 0x%08x\n"
- "%06ld.%06d %s::%s: pa 0x%llx\n"
- "%06ld.%06d %s::%s: pa 0x%llx, completion code %u\n"
- "%06ld.%06d %s::%s: pcie reset seperation workaround needed in ROM!\n"
- "%06ld.%06d %s::%s: polling for MHICTRL.RESET to be 0, MHICTRL: 0x%x\n"
- "%06ld.%06d %s::%s: pool needs to be atleast of dart page size %u\n"
- "%06ld.%06d %s::%s: provider %p, options 0x%08x\n"
- "%06ld.%06d %s::%s: provider %p, options 0x%08x, defer %p\n"
- "%06ld.%06d %s::%s: read %u, buffer %p, size %u\n"
- "%06ld.%06d %s::%s: region %u does not exist\n"
- "%06ld.%06d %s::%s: region Id: %u\n"
- "%06ld.%06d %s::%s: register %u, buff %p, size %u\n"
- "%06ld.%06d %s::%s: register time event callback failed, ret: 0x%08x\n"
- "%06ld.%06d %s::%s: res = 0x%x, code %u, size = %u\n"
- "%06ld.%06d %s::%s: res = 0x%x, size = %llu, cookie %p\n"
- "%06ld.%06d %s::%s: ring %d, 0x%llx\n"
- "%06ld.%06d %s::%s: ring %d, not aligned to %u\n"
- "%06ld.%06d %s::%s: ring %d, not large enough %u\n"
- "%06ld.%06d %s::%s: ring 0x%llx\n"
- "%06ld.%06d %s::%s: ring not aligned to %u\n"
- "%06ld.%06d %s::%s: ring not large enough %u\n"
- "%06ld.%06d %s::%s: shared mem region Id: %u, already present, client needs to it unmap first!\n"
- "%06ld.%06d %s::%s: size %u\n"
- "%06ld.%06d %s::%s: skip doorbell flush %u, pa 0x%llx\n"
- "%06ld.%06d %s::%s: status %u, dbg1 0x%x, dbg2 0x%x, dbg3 0x%x, errCode %u\n"
- "%06ld.%06d %s::%s: stopping memory pool for %llu\n"
- "%06ld.%06d %s::%s: super::start failed\n"
- "%06ld.%06d %s::%s: t %u, arg0 %p, arg1 %p\n"
- "%06ld.%06d %s::%s: there are more event rings than context array can hold\n"
- "%06ld.%06d %s::%s: time config: addr: 0x%p, 0x%lx\n"
- "%06ld.%06d %s::%s: time sync -> doorbell num: %u, event num: %u\n"
- "%06ld.%06d %s::%s: timerMode %u, arg1 %p\n"
- "%06ld.%06d %s::%s: to %s\n"
- "%06ld.%06d %s::%s: unable to allocate _cacheChannelRP array\n"
- "%06ld.%06d %s::%s: unable to allocate _channel instance array\n"
- "%06ld.%06d %s::%s: unable to allocate _msiRange\n"
- "%06ld.%06d %s::%s: unable to allocate _shadowChannelDoorbell array\n"
- "%06ld.%06d %s::%s: unable to allocate _shadowEventDoorbell array\n"
- "%06ld.%06d %s::%s: unexpected memory pool array object entry %u\n"
- "%06ld.%06d %s::%s: unexpected msi %d\n"
- "%06ld.%06d %s::%s: unexpected register read request\n"
- "%06ld.%06d %s::%s: unexpected size\n"
- "%06ld.%06d %s::%s: va 0x%llx\n"
- "%06ld.%06d %s::%s: version 0x%08x, expected 0x%08x\n"
- "%06ld.%06d %s::%s: will process event rings %d to %d\n"
- "1211111212221212121111111111111111111111221221222211111111112222"
- "12111122111"
- "AppleBasebandPCIMAVControl::%s: failed to create/init a reporter\n"
- "AppleBasebandPCIMAVControl::%s: failed to start reporting\n"
- "AppleBasebandPCIMAVControlReporter"
- "AppleBasebandPCIMAVControlReporter::%s: Failed to retrieve Device Descriptor\n"
- "abortChannel"
- "abortChannelGated"
- "abortChannels"
- "allocateChannelMemory"
- "allocateDeviceMemory"
- "asserted"
- "assignChannelMemory"
- "asyncCallCountUpdate"
- "asyncCompletion"
- "asyncFunction"
- "attach"
- "callAsync"
- "cancelAsync"
- "cancelImage"
- "cancelTimer"
- "changeState"
- "changeToM1"
- "checkCompletedIO"
- "checkIndexMSIRange"
- "checkPendingCommand"
- "checkPendingIO"
- "close"
- "closeGated"
- "coalescedTransferCompletion"
- "commandCompletion"
- "completeIO"
- "completeSharedEventIO"
- "computeChannelMemory"
- "computeDeviceMemory"
- "createDeviceFunction"
- "createPools"
- "createSetupChannel"
- "createSetupControl"
- "createSetupDevice"
- "createSetupInterface"
- "createSetupInterfaces"
- "deRegisterChannel"
- "deasserted"
- "deregisterTimeEventCallback"
- "detach"
- "deviceAlive"
- "deviceWake"
- "deviceWakeAsync"
- "device_wake assert vote"
- "device_wake deassert vote"
- "device_wake off"
- "device_wake on"
- "didTerminate"
- "engage"
- "enterError"
- "enterErrorCompletion"
- "enterLowPower"
- "errorFunction"
- "execEnvChangeFunction"
- "execEnvironmentChange"
- "exitLowPower"
- "findTimeCapability"
- "finishImageCommand"
- "finishMemoryCommand"
- "free"
- "getChannelMSIConfig"
- "getChannelProperties"
- "getDesiredLinkSpeed"
- "getReporterInterfaceNames"
- "initWithInfo"
- "initialize"
- "initializeDeviceWakeDoorbell"
- "invokeAsync"
- "ioCompletion"
- "ioTransfer"
- "linkDown"
- "linkRecovery"
- "linkUp"
- "mStateChangeFunction"
- "mapAckComplete_block_invoke"
- "mapSharedMemory"
- "mapSharedMemory_block_invoke"
- "mapUnmapMessageComplete"
- "mhiReset"
- "mhiResetDone"
- "msiInterrupt"
- "notifyError"
- "open"
- "openGated"
- "performTimeSync"
- "prepareImageCommand"
- "prepareMemoryCommand"
- "prepareTimeSync"
- "printChannelParams"
- "printDeviceParams"
- "processCurrentCommand"
- "processERE"
- "processTRE"
- "queueCommand"
- "queueTransfer"
- "read"
- "readExecutionEnvironment"
- "readGated"
- "readRegister"
- "readRegisterGated"
- "recoveryCheck"
- "registerChannel"
- "registerTimeEventCallback"
- "resetChannel"
- "resetChannelComplete"
- "rscIOCompletion"
- "scanCheck"
- "sendCommand"
- "sendImage"
- "sendImageCompletion"
- "sendImageCompletionGated"
- "sendImageGated"
- "sendMapUnmapMessage"
- "sendTransfer"
- "setDevice"
- "setUpTimeConfig"
- "setupChannel"
- "setupCommandRing"
- "setupContext"
- "setupController"
- "setupDevice"
- "setupDeviceParams"
- "setupEventRing"
- "setupMapUnmapCompletion"
- "setupTransferRing"
- "shadowDBCheckFunction_block_invoke"
- "shadowDBFunction_block_invoke"
- "shadowDoorbell"
- "shadowDoorbellCheck"
- "shadowDoorbellFlush"
- "shadowDoorbellProcess"
- "site.AppleBasebandPCIMAVControlReporter"
- "start"
- "startChannel"
- "startChannelComplete"
- "startChannelGated"
- "startChannels"
- "startCheck"
- "startTimer"
- "stateTransition"
- "stop"
- "stopChannel"
- "stopChannelComplete"
- "synchronousFunction"
- "teardownChannel"
- "teardownController"
- "teardownDevice"
- "teardownPools"
- "terminate"
- "terminateDevice"
- "terminateInterface"
- "terminateInterfaces"
- "terminate_block_invoke"
- "timeDomainToDeviceWakeVote"
- "timeSync"
- "timeSyncCompletion"
- "timeSyncEventCallback"
- "timeSync_block_invoke"
- "timer"
- "timerCompletion"
- "timerFunction_block_invoke"
- "transferCompletion"
- "triggerAsync"
- "triggerMSIFunction"
- "triggerRecovery"
- "unmapAckComplete_block_invoke"
- "unmapSharedMemory"
- "unmapSharedMemory_block_invoke"
- "willTerminate"
- "write"
- "writeGated"
- "~ABPBHIChannel"
- "~ABPBHIDevice"
- "~ABPMHIChannel"
- "~ABPMHIDevice"

```

>  `com.apple.driver.corecapture`

```diff

   __TEXT.__const: 0x110
   __TEXT.__cstring: 0x1ec9
   __TEXT.__os_log: 0x4094
-  __TEXT_EXEC.__text: 0x26f08
+  __TEXT_EXEC.__text: 0x26f14
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc4
   __DATA.__common: 0x2e0

```

>  `com.apple.filesystems.apfs`

```diff

   __TEXT.__cstring: 0x48590
   __TEXT_EXEC.__text: 0x13a494
   __TEXT_EXEC.__auth_stubs: 0x0
-  __DATA.__data: 0x690
+  __DATA.__data: 0x688
   __DATA.__bss: 0xc60
   __DATA_CONST.__auth_got: 0x10c8
   __DATA_CONST.__got: 0x1b0
CStrings:
+ "20:58:55"
- "22:22:59"

```

>  `com.apple.iokit.AppleARMIISAudio`

```diff

   __TEXT.__os_log: 0x2778
   __TEXT.__cstring: 0x2da3
   __TEXT.__const: 0xa8
-  __TEXT_EXEC.__text: 0x15648
+  __TEXT_EXEC.__text: 0x15680
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x188
   __DATA.__common: 0x60
-  __DATA_CONST.__auth_got: 0x2a0
+  __DATA_CONST.__auth_got: 0x2b0
   __DATA_CONST.__got: 0x88
   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__mod_init_func: 0x10

```

>  `com.apple.security.sandbox`

```diff

 2401.40.25.0.0
-  __TEXT.__const: 0x187479
+  __TEXT.__const: 0x1874f9
   __TEXT.__cstring: 0x6f6b
   __TEXT.__os_log: 0x2029
   __TEXT_EXEC.__text: 0x30568

```

</details>

## MachO

### 🆕 NEW (6)

- `/System/Library/Accounts/Notification/GroupKitAccountNotification.bundle/GroupKitAccountNotification`
- `/System/Library/CoreServices/CoreTypes.bundle/Contents/Library/MobileDevices-0002.bundle/MobileDevices-0002`
- `/System/Library/ExtensionKit/Extensions/ConditionalEngineAppIntentsExtension.appex/ConditionalEngineAppIntentsExtension`
- `/System/Library/ExtensionKit/Extensions/ConditionalEngineLighthouseExtension.appex/ConditionalEngineLighthouseExtension`
- `/System/Library/NanoPreferenceBundles/Applications/UrchinBridgeSettings.bundle/UrchinBridgeSettings`
- `/System/Library/PrivateFrameworks/GroupKit.framework/groupkitd`

### ❌ Removed (2)

- `/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/AirPlayDiagnosticExtension.appex/AirPlayDiagnosticExtension`
- `/usr/libexec/memoryanalyticsd`

### ⬆️ Updated (334)

<details>
  <summary><i>View Updated</i></summary>

- [/Applications/AccessorySetupUI.app/AccessorySetupUI](MACHOS/AccessorySetupUI.md)
- [/Applications/AirDropUI.app/AirDropUI](MACHOS/AirDropUI.md)
- [/Applications/AppDistributionLaunchAngel.app/AppDistributionLaunchAngel](MACHOS/AppDistributionLaunchAngel.md)
- [/Applications/AppStore.app/AppStore](MACHOS/AppStore.md)
- [/Applications/AppStore.app/PlugIns/AppStoreWidgetsExtension.appex/AppStoreWidgetsExtension](MACHOS/AppStoreWidgetsExtension.md)
- [/Applications/AppStore.app/PlugIns/ProductPageExtension.appex/ProductPageExtension](MACHOS/ProductPageExtension.md)
- [/Applications/AppStore.app/PlugIns/SubscribePageExtension.appex/SubscribePageExtension](MACHOS/SubscribePageExtension.md)
- [/Applications/AppleIDSetupUIService.app/AppleIDSetupUIService](MACHOS/AppleIDSetupUIService.md)
- [/Applications/AskToMessagesHost.app/PlugIns/AskToMessagesExtension.appex/AskToMessagesExtension](MACHOS/AskToMessagesExtension.md)
- [/Applications/AutoSettings.app/AutoSettings](MACHOS/AutoSettings.md)
- [/Applications/BusinessExtensionsWrapper.app/PlugIns/Business.appex/Business](MACHOS/Business.md)
- [/Applications/CarCamera.app/CarCamera](MACHOS/CarCamera.md)
- [/Applications/Charge.app/Charge](MACHOS/Charge.md)
- [/Applications/CheckerBoard.app/CheckerBoard](MACHOS/CheckerBoard.md)
- [/Applications/Climate.app/Climate](MACHOS/Climate.md)
- [/Applications/ClockAngel.app/ClockAngel](MACHOS/ClockAngel.md)
- [/Applications/Closures.app/Closures](MACHOS/Closures.md)
- [/Applications/ColorPickerUIService.app/ColorPickerUIService](MACHOS/ColorPickerUIService.md)
- [/Applications/CoreAuthUI.app/CoreAuthUI](MACHOS/CoreAuthUI.md)
- [/Applications/Diagnostics.app/Diagnostics](MACHOS/Diagnostics.md)
- [/Applications/DiagnosticsReporter.app/DiagnosticsReporter](MACHOS/DiagnosticsReporter.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-7004.appex/Diagnostic-7004](MACHOS/Diagnostic-7004.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8185.appex/Diagnostic-8185](MACHOS/Diagnostic-8185.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8268.appex/Diagnostic-8268](MACHOS/Diagnostic-8268.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8340.appex/Diagnostic-8340](MACHOS/Diagnostic-8340.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8343.appex/Diagnostic-8343](MACHOS/Diagnostic-8343.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-9006.appex/Diagnostic-9006](MACHOS/Diagnostic-9006.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-9008.appex/Diagnostic-9008](MACHOS/Diagnostic-9008.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-9010.appex/Diagnostic-9010](MACHOS/Diagnostic-9010.md)
- [/Applications/DiagnosticsService.app/PlugIns/SystemReport-AirPods.appex/SystemReport-AirPods](MACHOS/SystemReport-AirPods.md)
- [/Applications/DiagnosticsService.app/PlugIns/SystemReport-BatteryCase.appex/SystemReport-BatteryCase](MACHOS/SystemReport-BatteryCase.md)
- [/Applications/DiagnosticsService.app/PlugIns/SystemReport.appex/SystemReport](MACHOS/SystemReport.md)
- [/Applications/EventViewService.app/EventViewService](MACHOS/EventViewService.md)
- [/Applications/FTMInternal-4.app/FTMInternal-4](MACHOS/FTMInternal-4.md)
- [/Applications/Family.app/PlugIns/InviteMessageBubbleExtension.appex/InviteMessageBubbleExtension](MACHOS/InviteMessageBubbleExtension.md)
- [/Applications/FinanceUIService.app/FinanceUIService](MACHOS/FinanceUIService.md)
- [/Applications/FindMyRemoteUIService.app/FindMyRemoteUIService](MACHOS/FindMyRemoteUIService.md)
- [/Applications/GameCenterUIService.app/PlugIns/GameCenterMessageExtension.appex/GameCenterMessageExtension](MACHOS/GameCenterMessageExtension.md)
- [/Applications/GameCenterWidgets.app/PlugIns/GCWidgets.appex/GCWidgets](MACHOS/GCWidgets.md)
- [/Applications/GameOverlayUI.app/GameOverlayUI](MACHOS/GameOverlayUI.md)
- [/Applications/HDSViewService.app/HDSViewService](MACHOS/HDSViewService.md)
- [/Applications/HeadphoneProxService.app/HeadphoneProxService](MACHOS/HeadphoneProxService.md)
- [/Applications/HealthENBuddy.app/HealthENBuddy](MACHOS/HealthENBuddy.md)
- [/Applications/HealthENLauncher.app/HealthENLauncher](MACHOS/HealthENLauncher.md)
- [/Applications/InCallService.app/InCallService](MACHOS/InCallService.md)
- [/Applications/MTLReplayer.app/Frameworks/MTLReplayController.framework/MTLReplayController](MACHOS/MTLReplayController.md)
- [/Applications/MagnifierAngel.app/MagnifierAngel](MACHOS/MagnifierAngel.md)
- [/Applications/Media.app/Media](MACHOS/Media.md)
- [/Applications/MediaRemoteUI.app/MediaRemoteUI](MACHOS/MediaRemoteUI.md)
- [/Applications/MobilePhone.app/MobilePhone](MACHOS/MobilePhone.md)
- [/Applications/MobileSafari.app/PlugIns/SafariWidgetExtension.appex/SafariWidgetExtension](MACHOS/SafariWidgetExtension.md)
- [/Applications/MobileSlideShow.app/PlugIns/PhotosReliveWidget.appex/PhotosReliveWidget](MACHOS/PhotosReliveWidget.md)
- [/Applications/MomentsUIService.app/MomentsUIService](MACHOS/MomentsUIService.md)
- [/Applications/MusicRecognition.app/MusicRecognition](MACHOS/MusicRecognition.md)
- [/Applications/PASViewService.app/PASViewService](MACHOS/PASViewService.md)
- [/Applications/PCViewService.app/PCViewService](MACHOS/PCViewService.md)
- [/Applications/PeopleMessageService.app/Extensions/PeopleLegacyMessageService.appex/PeopleLegacyMessageService](MACHOS/PeopleLegacyMessageService.md)
- [/Applications/PeopleMessageService.app/PeopleMessageService](MACHOS/PeopleMessageService.md)
- [/Applications/PeopleMessageService.app/PlugIns/PeopleMessagesAskToBuy.appex/PeopleMessagesAskToBuy](MACHOS/PeopleMessagesAskToBuy.md)
- [/Applications/PeopleMessageService.app/PlugIns/PeopleMessagesScreenTime.appex/PeopleMessagesScreenTime](MACHOS/PeopleMessagesScreenTime.md)
- [/Applications/PeopleViewService.app/PeopleViewService](MACHOS/PeopleViewService.md)
- [/Applications/PeopleViewService.app/PlugIns/PeopleWidget_iOSExtension.appex/PeopleWidget_iOSExtension](MACHOS/PeopleWidget_iOSExtension.md)
- [/Applications/PeopleViewService.app/PlugIns/SelectPerson_iOS.appex/SelectPerson_iOS](MACHOS/SelectPerson_iOS.md)
- [/Applications/PreviewShell.app/PreviewShell](MACHOS/PreviewShell.md)
- [/Applications/SOSBuddy.app/SOSBuddy](MACHOS/SOSBuddy.md)
- [/Applications/Screen Time.app/PlugIns/ScreenTimeWidgetExtension.appex/ScreenTimeWidgetExtension](MACHOS/ScreenTimeWidgetExtension.md)
- [/Applications/Screen Time.app/PlugIns/ScreenTimeWidgetIntentsExtension.appex/ScreenTimeWidgetIntentsExtension](MACHOS/ScreenTimeWidgetIntentsExtension.md)
- [/Applications/Setup.app/Setup](MACHOS/Setup.md)
- [/Applications/SharingViewService.app/SharingViewService](MACHOS/SharingViewService.md)
- [/Applications/ShazamEventsApp.app/ShazamEventsApp](MACHOS/ShazamEventsApp.md)
- [/Applications/Sidecar.app/PlugIns/ContinuityDisplay.appex/ContinuityDisplay](MACHOS/ContinuityDisplay.md)
- [/Applications/Sidecar.app/Sidecar](MACHOS/Sidecar.md)
- [/Applications/Siri.app/Siri](MACHOS/Siri.md)
- [/Applications/TDGSharingViewService.app/TDGSharingViewService](MACHOS/TDGSharingViewService.md)
- [/Applications/TVSetupUIService.app/TVSetupUIService](MACHOS/TVSetupUIService.md)
- [/Applications/TirePressure.app/TirePressure](MACHOS/TirePressure.md)
- [/Applications/WritingToolsUIService.app/WritingToolsUIService](MACHOS/WritingToolsUIService.md)
- [/Library/Audio/Plug-Ins/HAL/VirtualAudio.plugin/VirtualAudio](MACHOS/VirtualAudio.md)
- [/System/Applications/Family/InviteMessageBubbleExtension.appex/InviteMessageBubbleExtension](MACHOS/InviteMessageBubbleExtension.md)
- [/System/ExclaveKit/System/Library/Frameworks/SoundAnalysis.framework/SoundAnalysis](MACHOS/SoundAnalysis.md)
- [/System/ExclaveKit/System/Library/Frameworks/Vision.framework/Vision](MACHOS/Vision.md)
- [/System/ExclaveKit/System/Library/PrivateFrameworks/CollectionsInternal.framework/CollectionsInternal](MACHOS/CollectionsInternal.md)
- [/System/ExclaveKit/System/Library/PrivateFrameworks/CoreSpeechExclave.framework/CoreSpeechExclave](MACHOS/CoreSpeechExclave.md)
- [/System/ExclaveKit/System/Library/PrivateFrameworks/CoreSpeechExclaveComponent.framework/CoreSpeechExclaveComponent](MACHOS/CoreSpeechExclaveComponent.md)
- [/System/ExclaveKit/System/Library/PrivateFrameworks/VoiceTriggerEventProviderExclave.framework/VoiceTriggerEventProviderExclave](MACHOS/VoiceTriggerEventProviderExclave.md)
- [/System/ExclaveKit/usr/lib/swift/libswiftos.dylib](MACHOS/libswiftos.dylib.md)
- [/System/Library/AccessibilityBundles/LiveSpeechUIService.axuiservice/LiveSpeechUIService](MACHOS/LiveSpeechUIService.md)
- [/System/Library/AppleMediaServices/DynamicUI/PlugIns/CoreDynamicUIPlugin.bundle/CoreDynamicUIPlugin](MACHOS/CoreDynamicUIPlugin.md)
- [/System/Library/AppleMediaServices/DynamicUI/PlugIns/StoreDynamicUIPlugin.bundle/StoreDynamicUIPlugin](MACHOS/StoreDynamicUIPlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/AudioFlowDelegatePlugin.bundle/AudioFlowDelegatePlugin](MACHOS/AudioFlowDelegatePlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/CarCommandsFlowDelegatePlugin.bundle/CarCommandsFlowDelegatePlugin](MACHOS/CarCommandsFlowDelegatePlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/DailyBriefingFlowPlugin.bundle/DailyBriefingFlowPlugin](MACHOS/DailyBriefingFlowPlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/HealthFlowDelegatePlugin.bundle/HealthFlowDelegatePlugin](MACHOS/HealthFlowDelegatePlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/HomeCommunicationFlowDelegatePlugin.bundle/HomeCommunicationFlowDelegatePlugin](MACHOS/HomeCommunicationFlowDelegatePlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/InformationFlowPlugin.bundle/InformationFlowPlugin](MACHOS/InformationFlowPlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/PhoneCallFlowDelegatePlugin.bundle/PhoneCallFlowDelegatePlugin](MACHOS/PhoneCallFlowDelegatePlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/SocialConversationFlowDelegatePlugin.bundle/SocialConversationFlowDelegatePlugin](MACHOS/SocialConversationFlowDelegatePlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/TimerFlowDelegatePlugin.bundle/TimerFlowDelegatePlugin](MACHOS/TimerFlowDelegatePlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/WellnessFlowPlugin.bundle/WellnessFlowPlugin](MACHOS/WellnessFlowPlugin.md)
- [/System/Library/Assistant/Plugins/PreferencesAssistant.assistantBundle/PreferencesAssistant](MACHOS/PreferencesAssistant.md)
- [/System/Library/Assistant/Plugins/activity.assistantBundle/activity](MACHOS/activity.md)
- [/System/Library/Assistant/PrivateLearningPlugins/SiriPrivateLearningInferencePlugin.bundle/SiriPrivateLearningInferencePlugin](MACHOS/SiriPrivateLearningInferencePlugin.md)
- [/System/Library/Assistant/PrivateLearningPlugins/SiriPrivateLearningPatternExtractionPlugin.bundle/SiriPrivateLearningPatternExtractionPlugin](MACHOS/SiriPrivateLearningPatternExtractionPlugin.md)
- [/System/Library/Assistant/UIPlugins/RemindersSiriUIPlugin.siriUIBundle/RemindersSiriUIPlugin](MACHOS/RemindersSiriUIPlugin.md)
- [/System/Library/CoreServices/AccessibilityUIServer.app/PlugIns/AccessibilityControlsExtension.appex/AccessibilityControlsExtension](MACHOS/AccessibilityControlsExtension.md)
- [/System/Library/CoreServices/AegirProxyApp.app/PlugIns/AegirPoster.appex/AegirPoster](MACHOS/AegirPoster.md)
- [/System/Library/CoreServices/BluetoothUIService.app/BluetoothUIService](MACHOS/BluetoothUIService.md)
- [/System/Library/CoreServices/ClarityBoard.app/ClarityBoard](MACHOS/ClarityBoard.md)
- [/System/Library/CoreServices/HangHUD.app/HangHUD](MACHOS/HangHUD.md)
- [/System/Library/CoreServices/IntelligentLight.app/IntelligentLight](MACHOS/IntelligentLight.md)
- [/System/Library/CoreServices/LiveTranscriptionUI.app/LiveTranscriptionUI](MACHOS/LiveTranscriptionUI.md)
- [/System/Library/DataClassMigrators/BuddyMigrator.migrator/BuddyMigrator](MACHOS/BuddyMigrator.md)
- [/System/Library/DriverExtensions/com.apple.DriverKit-AppleBCMWLAN.dext/com.apple.DriverKit-AppleBCMWLAN](MACHOS/com.apple.DriverKit-AppleBCMWLAN.md)
- [/System/Library/ExtensionKit/Extensions/AccessibilityControlsExtension.appex/AccessibilityControlsExtension](MACHOS/AccessibilityControlsExtension.md)
- [/System/Library/ExtensionKit/Extensions/AppStoreEvalLighthouseWorker.appex/AppStoreEvalLighthouseWorker](MACHOS/AppStoreEvalLighthouseWorker.md)
- [/System/Library/ExtensionKit/Extensions/AssistantSettingsControlsExtension.appex/AssistantSettingsControlsExtension](MACHOS/AssistantSettingsControlsExtension.md)
- [/System/Library/ExtensionKit/Extensions/BatterySettingsIntentsExtension.appex/BatterySettingsIntentsExtension](MACHOS/BatterySettingsIntentsExtension.md)
- [/System/Library/ExtensionKit/Extensions/DocumentAppIntents.appex/DocumentAppIntents](MACHOS/DocumentAppIntents.md)
- [/System/Library/ExtensionKit/Extensions/FamilyIntents.appex/FamilyIntents](MACHOS/FamilyIntents.md)
- [/System/Library/ExtensionKit/Extensions/MercuryPosterExtension.appex/MercuryPosterExtension](MACHOS/MercuryPosterExtension.md)
- [/System/Library/ExtensionKit/Extensions/MusicEngagementExtension.appex/MusicEngagementExtension](MACHOS/MusicEngagementExtension.md)
- [/System/Library/ExtensionKit/Extensions/PridePosterExtension.appex/PridePosterExtension](MACHOS/PridePosterExtension.md)
- [/System/Library/ExtensionKit/Extensions/SafariAssistantWorker.appex/SafariAssistantWorker](MACHOS/SafariAssistantWorker.md)
- [/System/Library/ExtensionKit/Extensions/ScreenTimeAppIntentsExtension.appex/ScreenTimeAppIntentsExtension](MACHOS/ScreenTimeAppIntentsExtension.md)
- [/System/Library/Frameworks/AutomatedDeviceEnrollment.framework/PlugIns/AddDevicesToAutomatedDeviceEnrollmentExtension.appex/AddDevicesToAutomatedDeviceEnrollmentExtension](MACHOS/AddDevicesToAutomatedDeviceEnrollmentExtension.md)
- [/System/Library/Frameworks/CallKit.framework/XPCServices/com.apple.CallKit.CallDirectory.xpc/com.apple.CallKit.CallDirectory](MACHOS/com.apple.CallKit.CallDirectory.md)
- [/System/Library/Frameworks/CallKit.framework/XPCServices/com.apple.CallKit.CallDirectoryMaintenance.xpc/com.apple.CallKit.CallDirectoryMaintenance](MACHOS/com.apple.CallKit.CallDirectoryMaintenance.md)
- [/System/Library/Frameworks/CoreTelephony.framework/Support/CommCenterMobileHelper](MACHOS/CommCenterMobileHelper.md)
- [/System/Library/Frameworks/FamilyControls.framework/PlugIns/ActivityPickerExtension.appex/ActivityPickerExtension](MACHOS/ActivityPickerExtension.md)
- [/System/Library/Frameworks/FileProvider.framework/PlugIns/LocalStorageFileProvider.appex/LocalStorageFileProvider](MACHOS/LocalStorageFileProvider.md)
- [/System/Library/Frameworks/ManagedAppDistribution.framework/Support/managedappdistributiond](MACHOS/managedappdistributiond.md)
- [/System/Library/Frameworks/ManagedSettings.framework/ManagedSettingsAgent](MACHOS/ManagedSettingsAgent.md)
- [/System/Library/Frameworks/Security.framework/CircleJoinRequested/CircleJoinRequested](MACHOS/CircleJoinRequested.md)
- [/System/Library/Frameworks/Security.framework/CloudKeychainProxy.bundle/CloudKeychainProxy](MACHOS/CloudKeychainProxy.md)
- [/System/Library/Frameworks/Security.framework/XPCServices/TrustedPeersHelper.xpc/TrustedPeersHelper](MACHOS/TrustedPeersHelper.md)
- [/System/Library/Frameworks/StoreKit.framework/Support/storekitd](MACHOS/storekitd.md)
- [/System/Library/Frameworks/_DeviceActivity_SwiftUI.framework/PlugIns/DeviceActivityReportService.appex/DeviceActivityReportService](MACHOS/DeviceActivityReportService.md)
- [/System/Library/HIDPlugins/ColourSensorFilterPlugin.plugin/ColourSensorFilterPlugin](MACHOS/ColourSensorFilterPlugin.md)
- [/System/Library/Messages/iMessageApps/SafetyMonitorMessages.bundle/SafetyMonitorMessages](MACHOS/SafetyMonitorMessages.md)
- [/System/Library/Messages/iMessageBalloons/ASMessagesProvider.bundle/ASMessagesProvider](MACHOS/ASMessagesProvider.md)
- [/System/Library/Messages/iMessageBalloons/DigitalTouchBalloonProvider.bundle/DigitalTouchBalloonProvider](MACHOS/DigitalTouchBalloonProvider.md)
- [/System/Library/NanoPreferenceBundles/General/CompanionInternationalSettings.bundle/CompanionInternationalSettings](MACHOS/CompanionInternationalSettings.md)
- [/System/Library/NanoTimeKit/ComplicationBundles/DepthComplicationBundleCompanion.bundle/DepthComplicationBundleCompanion](MACHOS/DepthComplicationBundleCompanion.md)
- [/System/Library/PreferenceBundles/AccountSettings/icloudMailSettings.bundle/icloudMailSettings](MACHOS/icloudMailSettings.md)
- [/System/Library/PreferenceBundles/AirDropSettings.bundle/AirDropSettings](MACHOS/AirDropSettings.md)
- [/System/Library/PreferenceBundles/AppInstallationSettings.bundle/AppInstallationSettings](MACHOS/AppInstallationSettings.md)
- [/System/Library/PreferenceBundles/BatteryUsageUI.bundle/BatteryUsageUI](MACHOS/BatteryUsageUI.md)
- [/System/Library/PreferenceBundles/JournalSettings.bundle/JournalSettings](MACHOS/JournalSettings.md)
- [/System/Library/PreferenceBundles/MultitaskingAndGesturesSettings.bundle/MultitaskingAndGesturesSettings](MACHOS/MultitaskingAndGesturesSettings.md)
- [/System/Library/PreferenceBundles/PrivacyAndSecuritySettings.bundle/PrivacyAndSecuritySettings](MACHOS/PrivacyAndSecuritySettings.md)
- [/System/Library/PreferenceBundles/StorageSettingsUI.bundle/StorageSettingsUI](MACHOS/StorageSettingsUI.md)
- [/System/Library/PreferenceBundles/WallpaperSettings.bundle/WallpaperSettings](MACHOS/WallpaperSettings.md)
- [/System/Library/PrivateFrameworks/ABMHelper.framework/Support/abm-helper](MACHOS/abm-helper.md)
- [/System/Library/PrivateFrameworks/ASOctaneSupport.framework/XPCServices/ASOctaneSupportXPCService.xpc/ASOctaneSupportXPCService](MACHOS/ASOctaneSupportXPCService.md)
- [/System/Library/PrivateFrameworks/AppStoreComponents.framework/Support/appstorecomponentsd](MACHOS/appstorecomponentsd.md)
- [/System/Library/PrivateFrameworks/AppStoreDaemon.framework/Support/appstored](MACHOS/appstored.md)
- [/System/Library/PrivateFrameworks/AppleMediaServices.framework/amsaccountsd](MACHOS/amsaccountsd.md)
- [/System/Library/PrivateFrameworks/AppleMediaServicesUI.framework/amsengagementd](MACHOS/amsengagementd.md)
- [/System/Library/PrivateFrameworks/AssistantServices.framework/assistantd](MACHOS/assistantd.md)
- [/System/Library/PrivateFrameworks/AuthKit.framework/akd](MACHOS/akd.md)
- [/System/Library/PrivateFrameworks/AuthKitUI.framework/PlugIns/AKFollowUpExtension.appex/AKFollowUpExtension](MACHOS/AKFollowUpExtension.md)
- [/System/Library/PrivateFrameworks/AvatarUI.framework/PlugIns/AvatarPosterExtension.appex/AvatarPosterExtension](MACHOS/AvatarPosterExtension.md)
- [/System/Library/PrivateFrameworks/BookDataStore.framework/Support/bookdatastored](MACHOS/bookdatastored.md)
- [/System/Library/PrivateFrameworks/BusinessChatService.framework/businessservicesd](MACHOS/businessservicesd.md)
- [/System/Library/PrivateFrameworks/CacheDelete.framework/deleted_helper](MACHOS/deleted_helper.md)
- [/System/Library/PrivateFrameworks/CloudDocsUI.framework/PlugIns/com.apple.CloudDocsUI.CloudSharing.appex/com.apple.CloudDocsUI.CloudSharing](MACHOS/com.apple.CloudDocsUI.CloudSharing.md)
- [/System/Library/PrivateFrameworks/CloudSharing.framework/XPCServices/SPIHelper-iOS.xpc/SPIHelper-iOS](MACHOS/SPIHelper-iOS.md)
- [/System/Library/PrivateFrameworks/CloudSharingUI.framework/PlugIns/com.apple.CloudSharingUI.CloudSharing.appex/com.apple.CloudSharingUI.CloudSharing](MACHOS/com.apple.CloudSharingUI.CloudSharing.md)
- [/System/Library/PrivateFrameworks/CloudTelemetry.framework/XPCServices/CloudTelemetryService.xpc/CloudTelemetryService](MACHOS/CloudTelemetryService.md)
- [/System/Library/PrivateFrameworks/CoreParsec.framework/parsec-fbf](MACHOS/parsec-fbf.md)
- [/System/Library/PrivateFrameworks/CoreParsec.framework/parsecd](MACHOS/parsecd.md)
- [/System/Library/PrivateFrameworks/CoreThreadCommissionerService.framework/CoreThreadCommissionerServiced](MACHOS/CoreThreadCommissionerServiced.md)
- [/System/Library/PrivateFrameworks/CoreThreadRadio.framework/threadradiod](MACHOS/threadradiod.md)
- [/System/Library/PrivateFrameworks/DVTInstrumentsFoundation.framework/XPCServices/com.apple.dt.DTMLModelRunnerService.xpc/com.apple.dt.DTMLModelRunnerService](MACHOS/com.apple.dt.DTMLModelRunnerService.md)
- [/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/com.apple.DiagnosticExtensions.Cellular.appex/com.apple.DiagnosticExtensions.Cellular](MACHOS/com.apple.DiagnosticExtensions.Cellular.md)
- [/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/com.apple.DiagnosticExtensions.Telephony.appex/com.apple.DiagnosticExtensions.Telephony](MACHOS/com.apple.DiagnosticExtensions.Telephony.md)
- [/System/Library/PrivateFrameworks/DocumentManagerUICore.framework/PlugIns/RecentsAppPopover.appex/RecentsAppPopover](MACHOS/RecentsAppPopover.md)
- [/System/Library/PrivateFrameworks/DocumentManagerUICore.framework/PlugIns/RecentsAvocado.appex/RecentsAvocado](MACHOS/RecentsAvocado.md)
- [/System/Library/PrivateFrameworks/DocumentManagerUICore.framework/PlugIns/SaveToFiles.appex/SaveToFiles](MACHOS/SaveToFiles.md)
- [/System/Library/PrivateFrameworks/DocumentManagerUICore.framework/PlugIns/com.apple.DocumentManager.Service.appex/com.apple.DocumentManager.Service](MACHOS/com.apple.DocumentManager.Service.md)
- [/System/Library/PrivateFrameworks/EcosystemAnalytics.framework/Support/ecosystemanalyticsd](MACHOS/ecosystemanalyticsd.md)
- [/System/Library/PrivateFrameworks/FamilyCircle.framework/familycircled](MACHOS/familycircled.md)
- [/System/Library/PrivateFrameworks/FinHealth.framework/ClientTools/finhealthclient](MACHOS/finhealthclient.md)
- [/System/Library/PrivateFrameworks/FontServices.framework/Resources/UITypographyPanel.bundle/UITypographyPanel](MACHOS/UITypographyPanel.md)
- [/System/Library/PrivateFrameworks/GPUToolsCapture.framework/GPUToolsCapture](MACHOS/GPUToolsCapture.md)
- [/System/Library/PrivateFrameworks/GameCenterUI.framework/PlugIns/GameCenterMatchmakerExtension.appex/GameCenterMatchmakerExtension](MACHOS/GameCenterMatchmakerExtension.md)
- [/System/Library/PrivateFrameworks/HangTracer.framework/PlugIns/HangLogsDiagnosticExtension.appex/HangLogsDiagnosticExtension](MACHOS/HangLogsDiagnosticExtension.md)
- [/System/Library/PrivateFrameworks/HangTracer.framework/PlugIns/PerformanceLoggingDiagnosticExtension.appex/PerformanceLoggingDiagnosticExtension](MACHOS/PerformanceLoggingDiagnosticExtension.md)
- [/System/Library/PrivateFrameworks/HomePlatformSettingsUI.framework/PlugIns/HPSUIViewService.appex/HPSUIViewService](MACHOS/HPSUIViewService.md)
- [/System/Library/PrivateFrameworks/IDS.framework/identityservicesd.app/identityservicesd](MACHOS/identityservicesd.md)
- [/System/Library/PrivateFrameworks/LockdownMode.framework/lockdownmoded](MACHOS/lockdownmoded.md)
- [/System/Library/PrivateFrameworks/MLKit.framework/PlugIns/com.apple.MLKit.MLModelPreview.appex/com.apple.MLKit.MLModelPreview](MACHOS/com.apple.MLKit.MLModelPreview.md)
- [/System/Library/PrivateFrameworks/MLKit.framework/PlugIns/com.apple.MLKit.MLPackagePreview.appex/com.apple.MLKit.MLPackagePreview](MACHOS/com.apple.MLKit.MLPackagePreview.md)
- [/System/Library/PrivateFrameworks/ManagedConfiguration.framework/PlugIns/ManagedSettingsExtension.appex/ManagedSettingsExtension](MACHOS/ManagedSettingsExtension.md)
- [/System/Library/PrivateFrameworks/MessagesBlastDoorSupport.framework/XPCServices/MessagesBlastDoorService.xpc/MessagesBlastDoorService](MACHOS/MessagesBlastDoorService.md)
- [/System/Library/PrivateFrameworks/MobileAccessoryUpdater.framework/Support/accessoryupdaterd](MACHOS/accessoryupdaterd.md)
- [/System/Library/PrivateFrameworks/MobileAccessoryUpdater.framework/XPCServices/EAUpdaterService.xpc/EAUpdaterService](MACHOS/EAUpdaterService.md)
- [/System/Library/PrivateFrameworks/MobileAccessoryUpdater.framework/XPCServices/StandaloneHIDAudService.xpc/StandaloneHIDAudService](MACHOS/StandaloneHIDAudService.md)
- [/System/Library/PrivateFrameworks/MobileAccessoryUpdater.framework/XPCServices/UARPUpdaterServiceLegacyAudio.xpc/UARPUpdaterServiceLegacyAudio](MACHOS/UARPUpdaterServiceLegacyAudio.md)
- [/System/Library/PrivateFrameworks/MobileBackup.framework/backupd](MACHOS/backupd.md)
- [/System/Library/PrivateFrameworks/NeighborhoodActivityConduit.framework/XPCServices/com.apple.NeighborhoodActivityConduitService.xpc/com.apple.NeighborhoodActivityConduitService](MACHOS/com.apple.NeighborhoodActivityConduitService.md)
- [/System/Library/PrivateFrameworks/NewDeviceOutreach.framework/PlugIns/NewDeviceOutreachExtension.appex/NewDeviceOutreachExtension](MACHOS/NewDeviceOutreachExtension.md)
- [/System/Library/PrivateFrameworks/NewDeviceOutreach.framework/ndoagent](MACHOS/ndoagent.md)
- [/System/Library/PrivateFrameworks/PaperBoardUI.framework/XPCServices/SBRendererService.xpc/SBRendererService](MACHOS/SBRendererService.md)
- [/System/Library/PrivateFrameworks/PassKitCore.framework/passd](MACHOS/passd.md)
- [/System/Library/PrivateFrameworks/People.framework/peopled](MACHOS/peopled.md)
- [/System/Library/PrivateFrameworks/PersonalizedSensing.framework/XPCServices/PersonalizedSensingService.xpc/PersonalizedSensingService](MACHOS/PersonalizedSensingService.md)
- [/System/Library/PrivateFrameworks/PreviewsOSSupport.framework/Support/previewsd](MACHOS/previewsd.md)
- [/System/Library/PrivateFrameworks/PrivateCloudCompute.framework/privatecloudcomputed.app/privatecloudcomputed](MACHOS/privatecloudcomputed.md)
- [/System/Library/PrivateFrameworks/ScreenTimeCore.framework/ScreenTimeAgent](MACHOS/ScreenTimeAgent.md)
- [/System/Library/PrivateFrameworks/Search.framework/PlugIns/SpotlightDiagnostic.appex/SpotlightDiagnostic](MACHOS/SpotlightDiagnostic.md)
- [/System/Library/PrivateFrameworks/SiriVOX.framework/SiriHeadlessService](MACHOS/SiriHeadlessService.md)
- [/System/Library/PrivateFrameworks/SoundScapesUtility.framework/PlugIns/SoundScapesViewServices.appex/SoundScapesViewServices](MACHOS/SoundScapesViewServices.md)
- [/System/Library/PrivateFrameworks/Stickers.framework/Support/stickersd](MACHOS/stickersd.md)
- [/System/Library/PrivateFrameworks/TelephonyUtilities.framework/callservicesd](MACHOS/callservicesd.md)
- [/System/Library/PrivateFrameworks/UsageTracking.framework/UsageTrackingAgent](MACHOS/UsageTrackingAgent.md)
- [/System/Library/PrivateFrameworks/WatchFacesWallpaperSupport.framework/PlugIns/ExtragalacticPoster.appex/ExtragalacticPoster](MACHOS/ExtragalacticPoster.md)
- [/System/Library/PrivateFrameworks/WatchFacesWallpaperSupport.framework/PlugIns/RhizomePoster.appex/RhizomePoster](MACHOS/RhizomePoster.md)
- [/System/Library/PrivateFrameworks/WirelessInsights.framework/Support/wirelessinsightsd](MACHOS/wirelessinsightsd.md)
- [/System/Library/PrivateFrameworks/WorkflowUI.framework/PlugIns/FocusConfigurationExtension.appex/FocusConfigurationExtension](MACHOS/FocusConfigurationExtension.md)
- [/System/Library/PrivateFrameworks/iOSDiagnostics.framework/XPCServices/com.apple.DiagnosticsSessionAvailibility.xpc/com.apple.DiagnosticsSessionAvailibility](MACHOS/com.apple.DiagnosticsSessionAvailibility.md)
- [/System/Library/PrivateFrameworks/iOSDiagnostics.framework/iosdiagnosticsd](MACHOS/iosdiagnosticsd.md)
- [/System/Library/PrivateFrameworks/iTunesStore.framework/Support/itunesstored](MACHOS/itunesstored.md)
- [/System/Library/Settings/InstalledApps.settings/InstalledApps](MACHOS/InstalledApps.md)
- [/System/Library/Snippets/UIPlugins/ResponseGenerationUIPlugin.bundle/ResponseGenerationUIPlugin](MACHOS/ResponseGenerationUIPlugin.md)
- [/System/Library/Video/Plug-Ins/AppleVideoEncoder.bundle/AppleVideoEncoder](MACHOS/AppleVideoEncoder.md)
- [/private/var/staged_system_apps/Books.app/Books](MACHOS/Books.md)
- [/private/var/staged_system_apps/Books.app/Frameworks/BookAnalytics.framework/BookAnalytics](MACHOS/BookAnalytics.md)
- [/private/var/staged_system_apps/Books.app/Frameworks/BookEPUB.framework/BookEPUB](MACHOS/BookEPUB.md)
- [/private/var/staged_system_apps/Books.app/Frameworks/BookStoreUI.framework/BookStoreUI](MACHOS/BookStoreUI.md)
- [/private/var/staged_system_apps/Books.app/Frameworks/BooksPersonalization.framework/BooksPersonalization](MACHOS/BooksPersonalization.md)
- [/private/var/staged_system_apps/Books.app/Frameworks/BooksUI.framework/BooksUI](MACHOS/BooksUI.md)
- [/private/var/staged_system_apps/Books.app/PlugIns/BooksWidgetExtension.appex/BooksWidgetExtension](MACHOS/BooksWidgetExtension.md)
- [/private/var/staged_system_apps/Calculator.app/Calculator](MACHOS/Calculator.md)
- [/private/var/staged_system_apps/Files.app/Files](MACHOS/Files.md)
- [/private/var/staged_system_apps/FindMy.app/FindMy](MACHOS/FindMy.md)
- [/private/var/staged_system_apps/FindMy.app/PlugIns/FindMyNotificationsContent.appex/FindMyNotificationsContent](MACHOS/FindMyNotificationsContent.md)
- [/private/var/staged_system_apps/FindMy.app/PlugIns/FindMyNotificationsService.appex/FindMyNotificationsService](MACHOS/FindMyNotificationsService.md)
- [/private/var/staged_system_apps/FindMy.app/PlugIns/FindMyWidgetIntentsPeople.appex/FindMyWidgetIntentsPeople](MACHOS/FindMyWidgetIntentsPeople.md)
- [/private/var/staged_system_apps/Fitness.app/Fitness](MACHOS/Fitness.md)
- [/private/var/staged_system_apps/Freeform.app/Extensions/USDRendererExtension.appex/USDRendererExtension](MACHOS/USDRendererExtension.md)
- [/private/var/staged_system_apps/Freeform.app/Freeform](MACHOS/Freeform.md)
- [/private/var/staged_system_apps/Journal.app/Journal](MACHOS/Journal.md)
- [/private/var/staged_system_apps/Journal.app/PlugIns/JournalShareExtension.appex/JournalShareExtension](MACHOS/JournalShareExtension.md)
- [/private/var/staged_system_apps/Journal.app/PlugIns/JournalWidgetsSecure.appex/JournalWidgetsSecure](MACHOS/JournalWidgetsSecure.md)
- [/private/var/staged_system_apps/Maps.app/Maps](MACHOS/Maps.md)
- [/private/var/staged_system_apps/Maps.app/PlugIns/GeneralMapsWidget.appex/GeneralMapsWidget](MACHOS/GeneralMapsWidget.md)
- [/private/var/staged_system_apps/Measure.app/Measure](MACHOS/Measure.md)
- [/private/var/staged_system_apps/MobileMail.app/MobileMail](MACHOS/MobileMail.md)
- [/private/var/staged_system_apps/MobileMail.app/PlugIns/MailWidgetExtension.appex/MailWidgetExtension](MACHOS/MailWidgetExtension.md)
- [/private/var/staged_system_apps/MobileNotes.app/MobileNotes](MACHOS/MobileNotes.md)
- [/private/var/staged_system_apps/MobileNotes.app/PlugIns/com.apple.mobilenotes.SharingExtension.appex/com.apple.mobilenotes.SharingExtension](MACHOS/com.apple.mobilenotes.SharingExtension.md)
- [/private/var/staged_system_apps/MobileNotes.app/PlugIns/com.apple.mobilenotes.WidgetExtension.appex/com.apple.mobilenotes.WidgetExtension](MACHOS/com.apple.mobilenotes.WidgetExtension.md)
- [/private/var/staged_system_apps/MobileTimer.app/PlugIns/WorldClockWidget.appex/WorldClockWidget](MACHOS/WorldClockWidget.md)
- [/private/var/staged_system_apps/Music.app/Frameworks/MusicApplication.framework/MusicApplication](MACHOS/MusicApplication.md)
- [/private/var/staged_system_apps/Music.app/Frameworks/MusicApplication.framework/XPCServices/MusicScriptUpdateService.xpc/MusicScriptUpdateService](MACHOS/MusicScriptUpdateService.md)
- [/private/var/staged_system_apps/Music.app/Music](MACHOS/Music.md)
- [/private/var/staged_system_apps/Music.app/PlugIns/MusicMessagesApp.appex/MusicMessagesApp](MACHOS/MusicMessagesApp.md)
- [/private/var/staged_system_apps/Music.app/PlugIns/MusicWidgets.appex/MusicWidgets](MACHOS/MusicWidgets.md)
- [/private/var/staged_system_apps/Passbook.app/PlugIns/PassbookWidgetsExtension-iPhone.appex/PassbookWidgetsExtension-iPhone](MACHOS/PassbookWidgetsExtension-iPhone.md)
- [/private/var/staged_system_apps/Podcasts.app/Frameworks/NowPlayingUI.framework/NowPlayingUI](MACHOS/NowPlayingUI.md)
- [/private/var/staged_system_apps/Podcasts.app/Frameworks/ShelfKit.framework/ShelfKit](MACHOS/ShelfKit.md)
- [/private/var/staged_system_apps/Podcasts.app/Frameworks/ShelfKitCollectionViews.framework/ShelfKitCollectionViews](MACHOS/ShelfKitCollectionViews.md)
- [/private/var/staged_system_apps/Podcasts.app/Podcasts](MACHOS/Podcasts.md)
- [/private/var/staged_system_apps/Reminders.app/PlugIns/RemindersIntentsUIExtension.appex/RemindersIntentsUIExtension](MACHOS/RemindersIntentsUIExtension.md)
- [/private/var/staged_system_apps/Reminders.app/PlugIns/RemindersWidgetExtension.appex/RemindersWidgetExtension](MACHOS/RemindersWidgetExtension.md)
- [/private/var/staged_system_apps/Reminders.app/Reminders](MACHOS/Reminders.md)
- [/private/var/staged_system_apps/SequoiaTranslator.app/PlugIns/TranslationWidgetsExtension.appex/TranslationWidgetsExtension](MACHOS/TranslationWidgetsExtension.md)
- [/private/var/staged_system_apps/SequoiaTranslator.app/SequoiaTranslator](MACHOS/SequoiaTranslator.md)
- [/private/var/staged_system_apps/Shortcuts.app/Shortcuts](MACHOS/Shortcuts.md)
- [/private/var/staged_system_apps/Stocks.app/PlugIns/StocksWidget.appex/StocksWidget](MACHOS/StocksWidget.md)
- [/private/var/staged_system_apps/Tips.app/Tips](MACHOS/Tips.md)
- [/private/var/staged_system_apps/VoiceMemos.app/VoiceMemos](MACHOS/VoiceMemos.md)
- [/private/var/staged_system_apps/Weather.app/PlugIns/WeatherWidget.appex/WeatherWidget](MACHOS/WeatherWidget.md)
- [/private/var/staged_system_apps/Weather.app/Weather](MACHOS/Weather.md)
- [/usr/bin/IOMFB_FDR_Loader](MACHOS/IOMFB_FDR_Loader.md)
- [/usr/bin/abmlite](MACHOS/abmlite.md)
- [/usr/bin/swift-inspect](MACHOS/swift-inspect.md)
- [/usr/lib/libmobileassetd.dylib](MACHOS/libmobileassetd.dylib.md)
- [/usr/libexec/DumpPanic](MACHOS/DumpPanic.md)
- [/usr/libexec/ReportMemoryException](MACHOS/ReportMemoryException.md)
- [/usr/libexec/SidecarRelay](MACHOS/SidecarRelay.md)
- [/usr/libexec/anomalydetectiond](MACHOS/anomalydetectiond.md)
- [/usr/libexec/appleaccountd](MACHOS/appleaccountd.md)
- [/usr/libexec/applekeystored](MACHOS/applekeystored.md)
- [/usr/libexec/asktod](MACHOS/asktod.md)
- [/usr/libexec/assessmentagent](MACHOS/assessmentagent.md)
- [/usr/libexec/audioaccessoryd](MACHOS/audioaccessoryd.md)
- [/usr/libexec/audioanalyticsd](MACHOS/audioanalyticsd.md)
- [/usr/libexec/checkpointd](MACHOS/checkpointd.md)
- [/usr/libexec/coreidvd](MACHOS/coreidvd.md)
- [/usr/libexec/corerepaird](MACHOS/corerepaird.md)
- [/usr/libexec/dockaccessoryd](MACHOS/dockaccessoryd.md)
- [/usr/libexec/feedbackd](MACHOS/feedbackd.md)
- [/usr/libexec/findmydeviced](MACHOS/findmydeviced.md)
- [/usr/libexec/findmylocated](MACHOS/findmylocated.md)
- [/usr/libexec/gamepolicyd](MACHOS/gamepolicyd.md)
- [/usr/libexec/hangreporter](MACHOS/hangreporter.md)
- [/usr/libexec/hangtracerd](MACHOS/hangtracerd.md)
- [/usr/libexec/idcredd](MACHOS/idcredd.md)
- [/usr/libexec/locationd](MACHOS/locationd.md)
- [/usr/libexec/mobileassetd](MACHOS/mobileassetd.md)
- [/usr/libexec/mobilerepaird](MACHOS/mobilerepaird.md)
- [/usr/libexec/modelmanagerd](MACHOS/modelmanagerd.md)
- [/usr/libexec/momentsd](MACHOS/momentsd.md)
- [/usr/libexec/nearbyd](MACHOS/nearbyd.md)
- [/usr/libexec/nptocompaniond](MACHOS/nptocompaniond.md)
- [/usr/libexec/online-auth-agent](MACHOS/online-auth-agent.md)
- [/usr/libexec/perfdiagsselfenabled](MACHOS/perfdiagsselfenabled.md)
- [/usr/libexec/photosfaced](MACHOS/photosfaced.md)
- [/usr/libexec/proactiveeventtrackerd](MACHOS/proactiveeventtrackerd.md)
- [/usr/libexec/promotedcontentd](MACHOS/promotedcontentd.md)
- [/usr/libexec/proximitycontrold](MACHOS/proximitycontrold.md)
- [/usr/libexec/remindd](MACHOS/remindd.md)
- [/usr/libexec/remotepairingdeviced](MACHOS/remotepairingdeviced.md)
- [/usr/libexec/rtcreportingd](MACHOS/rtcreportingd.md)
- [/usr/libexec/searchpartyd](MACHOS/searchpartyd.md)
- [/usr/libexec/security-sysdiagnose](MACHOS/security-sysdiagnose.md)
- [/usr/libexec/securityuploadd](MACHOS/securityuploadd.md)
- [/usr/libexec/seserviced](MACHOS/seserviced.md)
- [/usr/libexec/signpost_reporter](MACHOS/signpost_reporter.md)
- [/usr/libexec/spindump_fileparser](MACHOS/spindump_fileparser.md)
- [/usr/libexec/sportsd](MACHOS/sportsd.md)
- [/usr/libexec/swtransparencyd](MACHOS/swtransparencyd.md)
- [/usr/libexec/tailspind](MACHOS/tailspind.md)
- [/usr/libexec/timed](MACHOS/timed.md)
- [/usr/libexec/transparencyd](MACHOS/transparencyd.md)
- [/usr/libexec/wifivelocityd](MACHOS/wifivelocityd.md)
- [/usr/sbin/BlueTool](MACHOS/BlueTool.md)
- [/usr/sbin/WirelessRadioManagerd](MACHOS/WirelessRadioManagerd.md)
- [/usr/sbin/bluetoothd](MACHOS/bluetoothd.md)
- [/usr/sbin/otctl](MACHOS/otctl.md)
- [/usr/sbin/spindump](MACHOS/spindump.md)
- [/usr/sbin/wifid](MACHOS/wifid.md)

</details>

### 🔑 Entitlements

- [Entitlements DIFF](Entitlements.md)

## Firmware

### ⬆️ Updated (5)

<details>
  <summary><i>View Updated</i></summary>

#### AppleAVE2FW_H17.im4p

>  `AppleAVE2FW_H17.im4p`

```diff

   __TEXT._rtk_mtab: 0x2d0
   __TEXT.__constructor: 0x0
   __DATA.__const: 0x2a20
-  __DATA.__data: 0x1078
+  __DATA.__data: 0x1070
   __DATA._rtk_patchbay: 0x1e8
   __DATA._rtk_init_stack: 0x10000
   __DATA._rtk_irq_stack: 0x1000

```

#### adc-rheia-d9x.im4p

>  `adc-rheia-d9x.im4p`

```diff

 
-  __TEXT.__text: 0x727254
+  __TEXT.__text: 0x727a54
   __TEXT.__data_copy: 0x200000
   __TEXT.__const: 0x995980
-  __TEXT.__cstring: 0x9d4aa
+  __TEXT.__cstring: 0x9d692
   __TEXT._rtk_mtab: 0x2a0
   __TEXT.__constructor: 0x0
   __TEXT.__chain_starts: 0x0
   __TEXT.text_env: 0x4fdac
   __TEXT.__eh_frame: 0x390
-  __DATA.__const: 0x52920
+  __DATA.__const: 0x52930
   __DATA._rtk_heap: 0x1000
   __DATA.__data: 0xdf870
   __DATA._rtk_power: 0x3a8

   __DATA.__zerofill: 0x219df0
   Functions: 0
   Symbols:   0
-  CStrings:  17286
+  CStrings:  17294
 
CStrings:
+ "20:21:51"
+ "Error: Chroma ch=%u Ms=%d Step=%d out=(%d %d) fmt=%d cmp=%d\n"
+ "Error: Luma ch=%u Ms=%d Step=%d out=(%d %d) fmt=%d %d cmp=%d\n"
+ "Height > 0 && Height <= pDescr->paramBES.m2mGdcBufferHeight"
+ "M2MGDC w/o output: scl0 %d %d, scl1 %d %d, overwritten by %d %d, m2mbuf %d %d\n"
+ "Oct 14 2024"
+ "Width > 0 && Width <= pDescr->paramBES.m2mGdcBufferWidth"
+ "outHeight > 0 && outHeight <= pDescr->paramBES.m2mGdcBufferHeight"
+ "outWidth > 0 && outWidth <= pDescr->paramBES.m2mGdcBufferWidth"
+ "textSize: exp %zu act %zu, scalerId=%d\n"
- "21:19:36"
- "Oct  2 2024"

```

#### ansf.t8140.release.im4p

>  `ansf.t8140.release.im4p`

```diff

   __TEXT.read: 0x65a0
   __TEXT.__const: 0x53c8
   __TEXT.idle_hooks: 0x10
-  __TEXT.__cstring: 0x21233
+  __TEXT.__cstring: 0x21235
   __TEXT.__chain_starts: 0x0
   __TEXT.__constructor: 0x0
   __TEXT._rtk_mtab: 0x310
CStrings:
+ "2032.40.4~116"
+ "AppleStorageFirmware-2032.40.4~116"
- "2032.40.4~82"
- "AppleStorageFirmware-2032.40.4~82"

```

#### exclave_sharedcache

>  `exclave_sharedcache`

```diff

 416.40.2.0.0
-  __TEXT.__text: 0x46677c
+  __TEXT.__text: 0x46687c
   __TEXT.__lcxx_override: 0x200
   __TEXT.__const: 0xdf4f8
   __TEXT.__cstring: 0x287ee

   __TEXT.__swift5_replace: 0x0
   __TEXT.__term_offsets: 0x0
   __TEXT.__thread_starts: 0x28
-  __TEXT.__eh_frame: 0x1f1c8
+  __TEXT.__eh_frame: 0x1f1a8
   __DATA.__got: 0x10
   __DATA.__auth_ptr: 0x268
   __DATA.__mod_init_func: 0x58

   __DATA.__common: 0x1f71
   __DATA_CONST.__mod_init_func: 0x0
   __DATA_CONST.__mod_term_func: 0x0
-  Functions: 16640
+  Functions: 16639
   Symbols:   0
   CStrings:  4501
 
CStrings:
+ "/AppleInternal/Library/BuildRoots/b4a7daee-7dd0-11ef-a7b2-56363ce8160b/Applications/Xcode.app/Contents/Developer/Platforms/ExclaveCore.iPhoneOS.platform/Developer/SDKs/ExclaveCore.iPhoneOS18.1.Internal.sdk/System/ExclaveCore/usr/include/xrt/thread.h"
+ "/AppleInternal/Library/BuildRoots/b4a7daee-7dd0-11ef-a7b2-56363ce8160b/Applications/Xcode.app/Contents/Developer/Platforms/ExclaveCore.iPhoneOS.platform/Developer/SDKs/ExclaveCore.iPhoneOS18.1.Internal.sdk/System/ExclaveCore/usr/local/standalone/RTKit/usr/include/protocols/mbi_tightbeam_protocol.h"
- "/AppleInternal/Library/BuildRoots/46f067b1-7d7d-11ef-bf8c-725d7f06bcf4/Applications/Xcode.app/Contents/Developer/Platforms/ExclaveCore.iPhoneOS.platform/Developer/SDKs/ExclaveCore.iPhoneOS18.1.Internal.sdk/System/ExclaveCore/usr/include/xrt/thread.h"
- "/AppleInternal/Library/BuildRoots/46f067b1-7d7d-11ef-bf8c-725d7f06bcf4/Applications/Xcode.app/Contents/Developer/Platforms/ExclaveCore.iPhoneOS.platform/Developer/SDKs/ExclaveCore.iPhoneOS18.1.Internal.sdk/System/ExclaveCore/usr/local/standalone/RTKit/usr/include/protocols/mbi_tightbeam_protocol.h"

```

#### rans.t8140.release.im4p

>  `rans.t8140.release.im4p`

```diff

   __TEXT.read: 0x65a0
   __TEXT.__const: 0x53c8
   __TEXT.idle_hooks: 0x10
-  __TEXT.__cstring: 0x21233
+  __TEXT.__cstring: 0x21235
   __TEXT.__chain_starts: 0x0
   __TEXT.__constructor: 0x0
   __TEXT._rtk_mtab: 0x310
CStrings:
+ "2032.40.4~116"
+ "AppleStorageFirmware-2032.40.4~116"
- "2032.40.4~82"
- "AppleStorageFirmware-2032.40.4~82"

```


</details>

## DSC

### WebKit

| iOS | Version |
| :-- | :------ |
| 18.1 *(22B5075a)* | 619.2.8.10.7 |
| 18.1 *(22B82)* | 619.2.8.10.7 |

### Dylibs

#### 🆕 NEW (7)

- `/System/Library/PrivateFrameworks/ConditionalEngineAppIntents.framework/ConditionalEngineAppIntents`
- `/System/Library/PrivateFrameworks/ConditionalEngineClient.framework/ConditionalEngineClient`
- `/System/Library/PrivateFrameworks/ConditionalEngineRuntime.framework/ConditionalEngineRuntime`
- `/System/Library/PrivateFrameworks/ConditionalEngineShared.framework/ConditionalEngineShared`
- `/System/Library/PrivateFrameworks/GroupKit.framework/GroupKit`
- `/System/Library/PrivateFrameworks/GroupKitCore.framework/GroupKitCore`
- `/System/Library/PrivateFrameworks/UrchinKit.framework/UrchinKit`

#### ⬆️ Updated (617)

<details>
  <summary><i>View Updated</i></summary>

- [/System/Library/AccessibilityBundles/Moments.axbundle/Moments](DYLIBS/Moments.md)
- [/System/Library/Assistant/UIPlugins/SiriFindMyUIPlugin.siriUIBundle/Frameworks/SiriFindMyUI.framework/SiriFindMyUI](DYLIBS/SiriFindMyUI.md)
- [/System/Library/Frameworks/AVFAudio.framework/AVFAudio](DYLIBS/AVFAudio.md)
- [/System/Library/Frameworks/ActivityKit.framework/ActivityKit](DYLIBS/ActivityKit.md)
- [/System/Library/Frameworks/AppIntents.framework/AppIntents](DYLIBS/AppIntents.md)
- [/System/Library/Frameworks/Assignables.framework/Assignables](DYLIBS/Assignables.md)
- [/System/Library/Frameworks/AudioToolbox.framework/AudioToolbox](DYLIBS/AudioToolbox.md)
- [/System/Library/Frameworks/AudioToolbox.framework/libAudioDSP.dylib](DYLIBS/libAudioDSP.dylib.md)
- [/System/Library/Frameworks/AudioToolbox.framework/libEmbeddedSystemAUs.dylib](DYLIBS/libEmbeddedSystemAUs.dylib.md)
- [/System/Library/Frameworks/Charts.framework/Charts](DYLIBS/Charts.md)
- [/System/Library/Frameworks/CloudKit.framework/CloudKit](DYLIBS/CloudKit.md)
- [/System/Library/Frameworks/Combine.framework/Combine](DYLIBS/Combine.md)
- [/System/Library/Frameworks/ContactProvider.framework/ContactProvider](DYLIBS/ContactProvider.md)
- [/System/Library/Frameworks/ContactsUI.framework/ContactsUI](DYLIBS/ContactsUI.md)
- [/System/Library/Frameworks/CoreAudioKit.framework/CoreAudioKit](DYLIBS/CoreAudioKit.md)
- [/System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth](DYLIBS/CoreBluetooth.md)
- [/System/Library/Frameworks/CoreGraphics.framework/CoreGraphics](DYLIBS/CoreGraphics.md)
- [/System/Library/Frameworks/CoreLocation.framework/CoreLocation](DYLIBS/CoreLocation.md)
- [/System/Library/Frameworks/CoreML.framework/CoreML](DYLIBS/CoreML.md)
- [/System/Library/Frameworks/CoreMedia.framework/CoreMedia](DYLIBS/CoreMedia.md)
- [/System/Library/Frameworks/CoreMediaIO.framework/CoreMediaIO](DYLIBS/CoreMediaIO.md)
- [/System/Library/Frameworks/CoreMotion.framework/CoreMotion](DYLIBS/CoreMotion.md)
- [/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony](DYLIBS/CoreTelephony.md)
- [/System/Library/Frameworks/CoreTelephony.framework/Support/CTParser.framework/CTParser](DYLIBS/CTParser.md)
- [/System/Library/Frameworks/CoreTelephony.framework/Support/libCommCenterBase.dylib](DYLIBS/libCommCenterBase.dylib.md)
- [/System/Library/Frameworks/CoreTelephony.framework/Support/libCommCenterCommandDrivers.dylib](DYLIBS/libCommCenterCommandDrivers.dylib.md)
- [/System/Library/Frameworks/CoreTelephony.framework/Support/libCommCenterKCommandDrivers.dylib](DYLIBS/libCommCenterKCommandDrivers.dylib.md)
- [/System/Library/Frameworks/CoreTelephony.framework/Support/libCommCenterMCommandDrivers.dylib](DYLIBS/libCommCenterMCommandDrivers.dylib.md)
- [/System/Library/Frameworks/CoreTelephony.framework/Support/libSystemDetermination.dylib](DYLIBS/libSystemDetermination.dylib.md)
- [/System/Library/Frameworks/CreateML.framework/CreateML](DYLIBS/CreateML.md)
- [/System/Library/Frameworks/CreateMLComponents.framework/CreateMLComponents](DYLIBS/CreateMLComponents.md)
- [/System/Library/Frameworks/CryptoKit.framework/CryptoKit](DYLIBS/CryptoKit.md)
- [/System/Library/Frameworks/DeviceActivity.framework/DeviceActivity](DYLIBS/DeviceActivity.md)
- [/System/Library/Frameworks/ExtensionFoundation.framework/ExtensionFoundation](DYLIBS/ExtensionFoundation.md)
- [/System/Library/Frameworks/FileProvider.framework/FileProvider](DYLIBS/FileProvider.md)
- [/System/Library/Frameworks/FinanceKit.framework/FinanceKit](DYLIBS/FinanceKit.md)
- [/System/Library/Frameworks/FinanceKitUI.framework/FinanceKitUI](DYLIBS/FinanceKitUI.md)
- [/System/Library/Frameworks/Foundation.framework/Foundation](DYLIBS/Foundation.md)
- [/System/Library/Frameworks/HealthKit.framework/HealthKit](DYLIBS/HealthKit.md)
- [/System/Library/Frameworks/IOKit.framework/Versions/A/IOKit](DYLIBS/IOKit.md)
- [/System/Library/Frameworks/ImagePlayground.framework/ImagePlayground](DYLIBS/ImagePlayground.md)
- [/System/Library/Frameworks/LiveCommunicationKit.framework/LiveCommunicationKit](DYLIBS/LiveCommunicationKit.md)
- [/System/Library/Frameworks/ManagedAppDistribution.framework/ManagedAppDistribution](DYLIBS/ManagedAppDistribution.md)
- [/System/Library/Frameworks/MarketplaceKit.framework/MarketplaceKit](DYLIBS/MarketplaceKit.md)
- [/System/Library/Frameworks/MusicKit.framework/MusicKit](DYLIBS/MusicKit.md)
- [/System/Library/Frameworks/Network.framework/Network](DYLIBS/Network.md)
- [/System/Library/Frameworks/PencilKit.framework/PencilKit](DYLIBS/PencilKit.md)
- [/System/Library/Frameworks/ProximityReader.framework/ProximityReader](DYLIBS/ProximityReader.md)
- [/System/Library/Frameworks/PushKit.framework/PushKit](DYLIBS/PushKit.md)
- [/System/Library/Frameworks/QuartzCore.framework/QuartzCore](DYLIBS/QuartzCore.md)
- [/System/Library/Frameworks/RealityFoundation.framework/RealityFoundation](DYLIBS/RealityFoundation.md)
- [/System/Library/Frameworks/RealityKit.framework/RealityKit](DYLIBS/RealityKit.md)
- [/System/Library/Frameworks/RoomPlan.framework/RoomPlan](DYLIBS/RoomPlan.md)
- [/System/Library/Frameworks/SceneKit.framework/SceneKit](DYLIBS/SceneKit.md)
- [/System/Library/Frameworks/SecureElementCredential.framework/SecureElementCredential](DYLIBS/SecureElementCredential.md)
- [/System/Library/Frameworks/ShazamKit.framework/ShazamKit](DYLIBS/ShazamKit.md)
- [/System/Library/Frameworks/SoundAnalysis.framework/SoundAnalysis](DYLIBS/SoundAnalysis.md)
- [/System/Library/Frameworks/Speech.framework/Speech](DYLIBS/Speech.md)
- [/System/Library/Frameworks/StickerKit.framework/StickerKit](DYLIBS/StickerKit.md)
- [/System/Library/Frameworks/SwiftData.framework/SwiftData](DYLIBS/SwiftData.md)
- [/System/Library/Frameworks/SwiftUI.framework/SwiftUI](DYLIBS/SwiftUI.md)
- [/System/Library/Frameworks/SwiftUICore.framework/SwiftUICore](DYLIBS/SwiftUICore.md)
- [/System/Library/Frameworks/TabularData.framework/TabularData](DYLIBS/TabularData.md)
- [/System/Library/Frameworks/Vision.framework/Vision](DYLIBS/Vision.md)
- [/System/Library/Frameworks/WidgetKit.framework/WidgetKit](DYLIBS/WidgetKit.md)
- [/System/Library/Frameworks/_GroupActivities_UIKit.framework/_GroupActivities_UIKit](DYLIBS/_GroupActivities_UIKit.md)
- [/System/Library/Frameworks/_ManagedAppDistribution_SwiftUI.framework/_ManagedAppDistribution_SwiftUI](DYLIBS/_ManagedAppDistribution_SwiftUI.md)
- [/System/Library/Frameworks/_MapKit_SwiftUI.framework/_MapKit_SwiftUI](DYLIBS/_MapKit_SwiftUI.md)
- [/System/Library/Frameworks/_MusicKit_SwiftUI.framework/_MusicKit_SwiftUI](DYLIBS/_MusicKit_SwiftUI.md)
- [/System/Library/Frameworks/_PassKit_SwiftUI.framework/_PassKit_SwiftUI](DYLIBS/_PassKit_SwiftUI.md)
- [/System/Library/Frameworks/_RealityKit_SwiftUI.framework/_RealityKit_SwiftUI](DYLIBS/_RealityKit_SwiftUI.md)
- [/System/Library/Frameworks/_StoreKit_SwiftUI.framework/_StoreKit_SwiftUI](DYLIBS/_StoreKit_SwiftUI.md)
- [/System/Library/Health/FeedItemPlugins/HearingAppPlugin.healthplugin/HearingAppPlugin](DYLIBS/HearingAppPlugin.md)
- [/System/Library/Health/FeedItemPlugins/Heart.healthplugin/Heart](DYLIBS/Heart.md)
- [/System/Library/Health/FeedItemPlugins/Highlights.healthplugin/Highlights](DYLIBS/Highlights.md)
- [/System/Library/Health/FeedItemPlugins/MedicationsHealthAppPlugin.healthplugin/MedicationsHealthAppPlugin](DYLIBS/MedicationsHealthAppPlugin.md)
- [/System/Library/Health/FeedItemPlugins/MenstrualCyclesAppPlugin.healthplugin/MenstrualCyclesAppPlugin](DYLIBS/MenstrualCyclesAppPlugin.md)
- [/System/Library/Health/FeedItemPlugins/MentalHealthAppPlugin.healthplugin/MentalHealthAppPlugin](DYLIBS/MentalHealthAppPlugin.md)
- [/System/Library/Health/FeedItemPlugins/RespiratoryHealthAppPlugin.healthplugin/RespiratoryHealthAppPlugin](DYLIBS/RespiratoryHealthAppPlugin.md)
- [/System/Library/Health/FeedItemPlugins/Safety.healthplugin/Safety](DYLIBS/Safety.md)
- [/System/Library/Health/FeedItemPlugins/SleepHealthAppPlugin.healthplugin/SleepHealthAppPlugin](DYLIBS/SleepHealthAppPlugin.md)
- [/System/Library/Health/FeedItemPlugins/Summaries.healthplugin/Summaries](DYLIBS/Summaries.md)
- [/System/Library/Health/FeedItemPlugins/VisionHealthAppPlugin.healthplugin/VisionHealthAppPlugin](DYLIBS/VisionHealthAppPlugin.md)
- [/System/Library/NanoTimeKit/ComplicationBundles/WeatherComplications.bundle/WeatherComplications](DYLIBS/WeatherComplications.md)
- [/System/Library/NanoTimeKit/FaceBundles/NTKEsterbrookFaceBundleCompanion.bundle/NTKEsterbrookFaceBundleCompanion](DYLIBS/NTKEsterbrookFaceBundleCompanion.md)
- [/System/Library/NanoTimeKit/FaceBundles/NTKParmesanFaceBundleCompanion.bundle/NTKParmesanFaceBundleCompanion](DYLIBS/NTKParmesanFaceBundleCompanion.md)
- [/System/Library/NanoTimeKit/FaceBundles/NTKRhizomeFaceBundleCompanion.bundle/NTKRhizomeFaceBundleCompanion](DYLIBS/NTKRhizomeFaceBundleCompanion.md)
- [/System/Library/PreferenceBundles/KeyboardSettings.bundle/KeyboardSettings](DYLIBS/KeyboardSettings.md)
- [/System/Library/Previews/ShellPlugins/WidgetPreviewsShellPlugin.bundle/WidgetPreviewsShellPlugin](DYLIBS/WidgetPreviewsShellPlugin.md)
- [/System/Library/PrivateFrameworks/ABMHelper.framework/ABMHelper](DYLIBS/ABMHelper.md)
- [/System/Library/PrivateFrameworks/AIMLInstrumentationStreams.framework/AIMLInstrumentationStreams](DYLIBS/AIMLInstrumentationStreams.md)
- [/System/Library/PrivateFrameworks/APFoundation.framework/APFoundation](DYLIBS/APFoundation.md)
- [/System/Library/PrivateFrameworks/APTransport.framework/APTransport](DYLIBS/APTransport.md)
- [/System/Library/PrivateFrameworks/ARKitCore.framework/ARKitCore](DYLIBS/ARKitCore.md)
- [/System/Library/PrivateFrameworks/ASEProcessing.framework/ASEProcessing](DYLIBS/ASEProcessing.md)
- [/System/Library/PrivateFrameworks/ASRBridge.framework/ASRBridge](DYLIBS/ASRBridge.md)
- [/System/Library/PrivateFrameworks/AVConference.framework/AVConference](DYLIBS/AVConference.md)
- [/System/Library/PrivateFrameworks/AVConference.framework/Frameworks/ViceroyTrace.framework/ViceroyTrace](DYLIBS/ViceroyTrace.md)
- [/System/Library/PrivateFrameworks/AVFCapture.framework/AVFCapture](DYLIBS/AVFCapture.md)
- [/System/Library/PrivateFrameworks/AXSoundDetectionUI.framework/AXSoundDetectionUI](DYLIBS/AXSoundDetectionUI.md)
- [/System/Library/PrivateFrameworks/AccessibilitySettingsUI.framework/AccessibilitySettingsUI](DYLIBS/AccessibilitySettingsUI.md)
- [/System/Library/PrivateFrameworks/AccessibilitySharedUISupport.framework/AccessibilitySharedUISupport](DYLIBS/AccessibilitySharedUISupport.md)
- [/System/Library/PrivateFrameworks/AccessibilityUtilities.framework/AccessibilityUtilities](DYLIBS/AccessibilityUtilities.md)
- [/System/Library/PrivateFrameworks/ActionButtonConfigurationUI.framework/ActionButtonConfigurationUI](DYLIBS/ActionButtonConfigurationUI.md)
- [/System/Library/PrivateFrameworks/ActivityAwardsCore.framework/ActivityAwardsCore](DYLIBS/ActivityAwardsCore.md)
- [/System/Library/PrivateFrameworks/ActivityAwardsServices.framework/ActivityAwardsServices](DYLIBS/ActivityAwardsServices.md)
- [/System/Library/PrivateFrameworks/ActivitySharingServices.framework/ActivitySharingServices](DYLIBS/ActivitySharingServices.md)
- [/System/Library/PrivateFrameworks/ActivityUIServices.framework/ActivityUIServices](DYLIBS/ActivityUIServices.md)
- [/System/Library/PrivateFrameworks/AirPlayKit.framework/AirPlayKit](DYLIBS/AirPlayKit.md)
- [/System/Library/PrivateFrameworks/AirPlayReceiver.framework/AirPlayReceiver](DYLIBS/AirPlayReceiver.md)
- [/System/Library/PrivateFrameworks/AirPlayReceiverKit.framework/AirPlayReceiverKit](DYLIBS/AirPlayReceiverKit.md)
- [/System/Library/PrivateFrameworks/AirPlaySender.framework/AirPlaySender](DYLIBS/AirPlaySender.md)
- [/System/Library/PrivateFrameworks/AnnotationKit.framework/AnnotationKit](DYLIBS/AnnotationKit.md)
- [/System/Library/PrivateFrameworks/AppAnalytics.framework/AppAnalytics](DYLIBS/AppAnalytics.md)
- [/System/Library/PrivateFrameworks/AppIntentsServices.framework/AppIntentsServices](DYLIBS/AppIntentsServices.md)
- [/System/Library/PrivateFrameworks/AppPredictionInternal.framework/AppPredictionInternal](DYLIBS/AppPredictionInternal.md)
- [/System/Library/PrivateFrameworks/AppProtection.framework/AppProtection](DYLIBS/AppProtection.md)
- [/System/Library/PrivateFrameworks/AppState.framework/AppState](DYLIBS/AppState.md)
- [/System/Library/PrivateFrameworks/AppStoreDaemon.framework/AppStoreDaemon](DYLIBS/AppStoreDaemon.md)
- [/System/Library/PrivateFrameworks/AppStoreKit.framework/AppStoreKit](DYLIBS/AppStoreKit.md)
- [/System/Library/PrivateFrameworks/AppStoreKitInternal.framework/AppStoreKitInternal](DYLIBS/AppStoreKitInternal.md)
- [/System/Library/PrivateFrameworks/AppleAccount.framework/AppleAccount](DYLIBS/AppleAccount.md)
- [/System/Library/PrivateFrameworks/AppleBasebandServices.framework/AppleBasebandServices](DYLIBS/AppleBasebandServices.md)
- [/System/Library/PrivateFrameworks/AppleCV3D.framework/AppleCV3D](DYLIBS/AppleCV3D.md)
- [/System/Library/PrivateFrameworks/AppleCVAPhoto.framework/AppleCVAPhoto](DYLIBS/AppleCVAPhoto.md)
- [/System/Library/PrivateFrameworks/AppleCVHWA.framework/AppleCVHWA](DYLIBS/AppleCVHWA.md)
- [/System/Library/PrivateFrameworks/AppleCareSupport.framework/AppleCareSupport](DYLIBS/AppleCareSupport.md)
- [/System/Library/PrivateFrameworks/AppleIDSetup.framework/AppleIDSetup](DYLIBS/AppleIDSetup.md)
- [/System/Library/PrivateFrameworks/AppleIDSetupDaemon.framework/AppleIDSetupDaemon](DYLIBS/AppleIDSetupDaemon.md)
- [/System/Library/PrivateFrameworks/AppleIDSetupUI.framework/AppleIDSetupUI](DYLIBS/AppleIDSetupUI.md)
- [/System/Library/PrivateFrameworks/AppleKeyStore.framework/AppleKeyStore](DYLIBS/AppleKeyStore.md)
- [/System/Library/PrivateFrameworks/AppleMediaServices.framework/AppleMediaServices](DYLIBS/AppleMediaServices.md)
- [/System/Library/PrivateFrameworks/AppleMediaServicesUI.framework/AppleMediaServicesUI](DYLIBS/AppleMediaServicesUI.md)
- [/System/Library/PrivateFrameworks/AppleMediaServicesUIDynamic.framework/AppleMediaServicesUIDynamic](DYLIBS/AppleMediaServicesUIDynamic.md)
- [/System/Library/PrivateFrameworks/AppleServiceToolkit.framework/AppleServiceToolkit](DYLIBS/AppleServiceToolkit.md)
- [/System/Library/PrivateFrameworks/ArgumentParserInternal.framework/ArgumentParserInternal](DYLIBS/ArgumentParserInternal.md)
- [/System/Library/PrivateFrameworks/AskToCore.framework/AskToCore](DYLIBS/AskToCore.md)
- [/System/Library/PrivateFrameworks/AssetViewer.framework/AssetViewer](DYLIBS/AssetViewer.md)
- [/System/Library/PrivateFrameworks/AssistantServices.framework/AssistantServices](DYLIBS/AssistantServices.md)
- [/System/Library/PrivateFrameworks/AssistantSettingsSupport.framework/AssistantSettingsSupport](DYLIBS/AssistantSettingsSupport.md)
- [/System/Library/PrivateFrameworks/AssistantUI.framework/AssistantUI](DYLIBS/AssistantUI.md)
- [/System/Library/PrivateFrameworks/AudioAnalyticsBase.framework/AudioAnalyticsBase](DYLIBS/AudioAnalyticsBase.md)
- [/System/Library/PrivateFrameworks/AudioSession.framework/AudioSession](DYLIBS/AudioSession.md)
- [/System/Library/PrivateFrameworks/AudioToolboxCore.framework/AudioToolboxCore](DYLIBS/AudioToolboxCore.md)
- [/System/Library/PrivateFrameworks/AuthKit.framework/AuthKit](DYLIBS/AuthKit.md)
- [/System/Library/PrivateFrameworks/AuthenticationServicesCore.framework/AuthenticationServicesCore](DYLIBS/AuthenticationServicesCore.md)
- [/System/Library/PrivateFrameworks/AutoBugCaptureCore.framework/AutoBugCaptureCore](DYLIBS/AutoBugCaptureCore.md)
- [/System/Library/PrivateFrameworks/AvatarKit.framework/AvatarKit](DYLIBS/AvatarKit.md)
- [/System/Library/PrivateFrameworks/BacklightServicesHost.framework/BacklightServicesHost](DYLIBS/BacklightServicesHost.md)
- [/System/Library/PrivateFrameworks/BasebandTraceHelper.framework/BasebandTraceHelper](DYLIBS/BasebandTraceHelper.md)
- [/System/Library/PrivateFrameworks/BatteryCenterUI.framework/BatteryCenterUI](DYLIBS/BatteryCenterUI.md)
- [/System/Library/PrivateFrameworks/BiometricKitUI.framework/BiometricKitUI](DYLIBS/BiometricKitUI.md)
- [/System/Library/PrivateFrameworks/Blackbeard.framework/Blackbeard](DYLIBS/Blackbeard.md)
- [/System/Library/PrivateFrameworks/BlastDoor.framework/BlastDoor](DYLIBS/BlastDoor.md)
- [/System/Library/PrivateFrameworks/BookFoundation.framework/BookFoundation](DYLIBS/BookFoundation.md)
- [/System/Library/PrivateFrameworks/BrailleSymbology.framework/BrailleSymbology](DYLIBS/BrailleSymbology.md)
- [/System/Library/PrivateFrameworks/CAFCombine.framework/CAFCombine](DYLIBS/CAFCombine.md)
- [/System/Library/PrivateFrameworks/CAFUI.framework/CAFUI](DYLIBS/CAFUI.md)
- [/System/Library/PrivateFrameworks/CDMFoundation.framework/CDMFoundation](DYLIBS/CDMFoundation.md)
- [/System/Library/PrivateFrameworks/CTCarrierSpace.framework/CTCarrierSpace](DYLIBS/CTCarrierSpace.md)
- [/System/Library/PrivateFrameworks/CTLazuliSupport.framework/CTLazuliSupport](DYLIBS/CTLazuliSupport.md)
- [/System/Library/PrivateFrameworks/CalendarLink.framework/CalendarLink](DYLIBS/CalendarLink.md)
- [/System/Library/PrivateFrameworks/CalendarUIKit.framework/CalendarUIKit](DYLIBS/CalendarUIKit.md)
- [/System/Library/PrivateFrameworks/CalendarWidget.framework/CalendarWidget](DYLIBS/CalendarWidget.md)
- [/System/Library/PrivateFrameworks/CarPlayAssetUI.framework/CarPlayAssetUI](DYLIBS/CarPlayAssetUI.md)
- [/System/Library/PrivateFrameworks/Cards.framework/Cards](DYLIBS/Cards.md)
- [/System/Library/PrivateFrameworks/CellularPlanManager.framework/CellularPlanManager](DYLIBS/CellularPlanManager.md)
- [/System/Library/PrivateFrameworks/ChatKit.framework/ChatKit](DYLIBS/ChatKit.md)
- [/System/Library/PrivateFrameworks/CheckerBoardServices.framework/CheckerBoardServices](DYLIBS/CheckerBoardServices.md)
- [/System/Library/PrivateFrameworks/Chirp.framework/Chirp](DYLIBS/Chirp.md)
- [/System/Library/PrivateFrameworks/ChronoCore.framework/ChronoCore](DYLIBS/ChronoCore.md)
- [/System/Library/PrivateFrameworks/ChronoCore.framework/Support/WidgetPreviewsExtensionAgent.bundle/WidgetPreviewsExtensionAgent](DYLIBS/WidgetPreviewsExtensionAgent.md)
- [/System/Library/PrivateFrameworks/ChronoKit.framework/ChronoKit](DYLIBS/ChronoKit.md)
- [/System/Library/PrivateFrameworks/ChronoServices.framework/ChronoServices](DYLIBS/ChronoServices.md)
- [/System/Library/PrivateFrameworks/CiderAudioServer.framework/CiderAudioServer](DYLIBS/CiderAudioServer.md)
- [/System/Library/PrivateFrameworks/ClassroomKit.framework/Frameworks/ClassroomUIKit.framework/ClassroomUIKit](DYLIBS/ClassroomUIKit.md)
- [/System/Library/PrivateFrameworks/ClockPoster.framework/ClockPoster](DYLIBS/ClockPoster.md)
- [/System/Library/PrivateFrameworks/CloudAsset.framework/CloudAsset](DYLIBS/CloudAsset.md)
- [/System/Library/PrivateFrameworks/CloudAssets.framework/CloudAssets](DYLIBS/CloudAssets.md)
- [/System/Library/PrivateFrameworks/CloudAttestation.framework/CloudAttestation](DYLIBS/CloudAttestation.md)
- [/System/Library/PrivateFrameworks/CloudDocsUI.framework/CloudDocsUI](DYLIBS/CloudDocsUI.md)
- [/System/Library/PrivateFrameworks/CloudRecommendationUI.framework/CloudRecommendationUI](DYLIBS/CloudRecommendationUI.md)
- [/System/Library/PrivateFrameworks/CloudSharingUI.framework/CloudSharingUI](DYLIBS/CloudSharingUI.md)
- [/System/Library/PrivateFrameworks/CloudSubscriptionFeatures.framework/CloudSubscriptionFeatures](DYLIBS/CloudSubscriptionFeatures.md)
- [/System/Library/PrivateFrameworks/CloudTelemetryTools.framework/CloudTelemetryTools](DYLIBS/CloudTelemetryTools.md)
- [/System/Library/PrivateFrameworks/Coherence.framework/Coherence](DYLIBS/Coherence.md)
- [/System/Library/PrivateFrameworks/CollectionsInternal.framework/CollectionsInternal](DYLIBS/CollectionsInternal.md)
- [/System/Library/PrivateFrameworks/CommunicationsUI.framework/CommunicationsUI](DYLIBS/CommunicationsUI.md)
- [/System/Library/PrivateFrameworks/ContactlessReaderUI.framework/ContactlessReaderUI](DYLIBS/ContactlessReaderUI.md)
- [/System/Library/PrivateFrameworks/ContactsAutocomplete.framework/ContactsAutocomplete](DYLIBS/ContactsAutocomplete.md)
- [/System/Library/PrivateFrameworks/ControlCenterUI.framework/ControlCenterUI](DYLIBS/ControlCenterUI.md)
- [/System/Library/PrivateFrameworks/ControlCenterUIKit.framework/ControlCenterUIKit](DYLIBS/ControlCenterUIKit.md)
- [/System/Library/PrivateFrameworks/ControlCenterUIServices.framework/ControlCenterUIServices](DYLIBS/ControlCenterUIServices.md)
- [/System/Library/PrivateFrameworks/ConversationKit.framework/ConversationKit](DYLIBS/ConversationKit.md)
- [/System/Library/PrivateFrameworks/CoordinationCore.framework/CoordinationCore](DYLIBS/CoordinationCore.md)
- [/System/Library/PrivateFrameworks/CoreBrightness.framework/CoreBrightness](DYLIBS/CoreBrightness.md)
- [/System/Library/PrivateFrameworks/CoreCDP.framework/CoreCDP](DYLIBS/CoreCDP.md)
- [/System/Library/PrivateFrameworks/CoreCDPInternal.framework/CoreCDPInternal](DYLIBS/CoreCDPInternal.md)
- [/System/Library/PrivateFrameworks/CoreCDPUI.framework/CoreCDPUI](DYLIBS/CoreCDPUI.md)
- [/System/Library/PrivateFrameworks/CoreCaptureDaemon.framework/CoreCaptureDaemon](DYLIBS/CoreCaptureDaemon.md)
- [/System/Library/PrivateFrameworks/CoreDiagnostics.framework/CoreDiagnostics](DYLIBS/CoreDiagnostics.md)
- [/System/Library/PrivateFrameworks/CoreHandwriting.framework/CoreHandwriting](DYLIBS/CoreHandwriting.md)
- [/System/Library/PrivateFrameworks/CoreIDV.framework/CoreIDV](DYLIBS/CoreIDV.md)
- [/System/Library/PrivateFrameworks/CoreIDVPAD.framework/CoreIDVPAD](DYLIBS/CoreIDVPAD.md)
- [/System/Library/PrivateFrameworks/CoreIDVRGBLiveness.framework/CoreIDVRGBLiveness](DYLIBS/CoreIDVRGBLiveness.md)
- [/System/Library/PrivateFrameworks/CoreIDVShared.framework/CoreIDVShared](DYLIBS/CoreIDVShared.md)
- [/System/Library/PrivateFrameworks/CoreIDVUI.framework/CoreIDVUI](DYLIBS/CoreIDVUI.md)
- [/System/Library/PrivateFrameworks/CoreOC.framework/CoreOC](DYLIBS/CoreOC.md)
- [/System/Library/PrivateFrameworks/CoreODI.framework/CoreODI](DYLIBS/CoreODI.md)
- [/System/Library/PrivateFrameworks/CoreODIEssentials.framework/CoreODIEssentials](DYLIBS/CoreODIEssentials.md)
- [/System/Library/PrivateFrameworks/CoreParsec.framework/CoreParsec](DYLIBS/CoreParsec.md)
- [/System/Library/PrivateFrameworks/CoreRepairCore.framework/CoreRepairCore](DYLIBS/CoreRepairCore.md)
- [/System/Library/PrivateFrameworks/CoreRepairKit.framework/CoreRepairKit](DYLIBS/CoreRepairKit.md)
- [/System/Library/PrivateFrameworks/CoreRepairUI.framework/CoreRepairUI](DYLIBS/CoreRepairUI.md)
- [/System/Library/PrivateFrameworks/CoreSpeechExclave.framework/CoreSpeechExclave](DYLIBS/CoreSpeechExclave.md)
- [/System/Library/PrivateFrameworks/CoreSpeechFoundation.framework/CoreSpeechFoundation](DYLIBS/CoreSpeechFoundation.md)
- [/System/Library/PrivateFrameworks/CoreUARP.framework/CoreUARP](DYLIBS/CoreUARP.md)
- [/System/Library/PrivateFrameworks/CoreWiFi.framework/CoreWiFi](DYLIBS/CoreWiFi.md)
- [/System/Library/PrivateFrameworks/CryptoKitPrivate.framework/CryptoKitPrivate](DYLIBS/CryptoKitPrivate.md)
- [/System/Library/PrivateFrameworks/DashBoard.framework/DashBoard](DYLIBS/DashBoard.md)
- [/System/Library/PrivateFrameworks/DataDetectorsCore.framework/DataDetectorsCore](DYLIBS/DataDetectorsCore.md)
- [/System/Library/PrivateFrameworks/DataDetectorsUI.framework/DataDetectorsUI](DYLIBS/DataDetectorsUI.md)
- [/System/Library/PrivateFrameworks/Dendrite.framework/Dendrite](DYLIBS/Dendrite.md)
- [/System/Library/PrivateFrameworks/DeviceDiscoveryUI.framework/DeviceDiscoveryUI](DYLIBS/DeviceDiscoveryUI.md)
- [/System/Library/PrivateFrameworks/DeviceExpertIntents.framework/DeviceExpertIntents](DYLIBS/DeviceExpertIntents.md)
- [/System/Library/PrivateFrameworks/DiagnosticRequestService.framework/DiagnosticRequestService](DYLIBS/DiagnosticRequestService.md)
- [/System/Library/PrivateFrameworks/DiagnosticsReporterServices.framework/DiagnosticsReporterServices](DYLIBS/DiagnosticsReporterServices.md)
- [/System/Library/PrivateFrameworks/DialogEngine.framework/DialogEngine](DYLIBS/DialogEngine.md)
- [/System/Library/PrivateFrameworks/DistributedEvaluation.framework/DistributedEvaluation](DYLIBS/DistributedEvaluation.md)
- [/System/Library/PrivateFrameworks/DistributedTimersDaemon.framework/DistributedTimersDaemon](DYLIBS/DistributedTimersDaemon.md)
- [/System/Library/PrivateFrameworks/DockKitCore.framework/DockKitCore](DYLIBS/DockKitCore.md)
- [/System/Library/PrivateFrameworks/DocumentManagerExecutables.framework/DocumentManagerExecutables](DYLIBS/DocumentManagerExecutables.md)
- [/System/Library/PrivateFrameworks/DrawingBoard.framework/DrawingBoard](DYLIBS/DrawingBoard.md)
- [/System/Library/PrivateFrameworks/DropInCore.framework/DropInCore](DYLIBS/DropInCore.md)
- [/System/Library/PrivateFrameworks/DropletUI.framework/DropletUI](DYLIBS/DropletUI.md)
- [/System/Library/PrivateFrameworks/EcosystemAnalytics.framework/EcosystemAnalytics](DYLIBS/EcosystemAnalytics.md)
- [/System/Library/PrivateFrameworks/EmojiPoster.framework/EmojiPoster](DYLIBS/EmojiPoster.md)
- [/System/Library/PrivateFrameworks/FMFCore.framework/FMFCore](DYLIBS/FMFCore.md)
- [/System/Library/PrivateFrameworks/FMFindingUI.framework/FMFindingUI](DYLIBS/FMFindingUI.md)
- [/System/Library/PrivateFrameworks/FMIPCore.framework/FMIPCore](DYLIBS/FMIPCore.md)
- [/System/Library/PrivateFrameworks/FMNetworking.framework/FMNetworking](DYLIBS/FMNetworking.md)
- [/System/Library/PrivateFrameworks/FPFS.framework/FPFS](DYLIBS/FPFS.md)
- [/System/Library/PrivateFrameworks/FaceTimeMessageStore.framework/FaceTimeMessageStore](DYLIBS/FaceTimeMessageStore.md)
- [/System/Library/PrivateFrameworks/FamilyCircleUI.framework/FamilyCircleUI](DYLIBS/FamilyCircleUI.md)
- [/System/Library/PrivateFrameworks/Feedback.framework/Feedback](DYLIBS/Feedback.md)
- [/System/Library/PrivateFrameworks/FeedbackCore.framework/FeedbackCore](DYLIBS/FeedbackCore.md)
- [/System/Library/PrivateFrameworks/FeedbackService.framework/FeedbackService](DYLIBS/FeedbackService.md)
- [/System/Library/PrivateFrameworks/FinanceDaemon.framework/FinanceDaemon](DYLIBS/FinanceDaemon.md)
- [/System/Library/PrivateFrameworks/FindMyCommon.framework/FindMyCommon](DYLIBS/FindMyCommon.md)
- [/System/Library/PrivateFrameworks/FindMyLocate.framework/FindMyLocate](DYLIBS/FindMyLocate.md)
- [/System/Library/PrivateFrameworks/FindMyMessaging.framework/FindMyMessaging](DYLIBS/FindMyMessaging.md)
- [/System/Library/PrivateFrameworks/FindMyUICore.framework/FindMyUICore](DYLIBS/FindMyUICore.md)
- [/System/Library/PrivateFrameworks/FitnessAppRoot.framework/FitnessAppRoot](DYLIBS/FitnessAppRoot.md)
- [/System/Library/PrivateFrameworks/FitnessAsset.framework/FitnessAsset](DYLIBS/FitnessAsset.md)
- [/System/Library/PrivateFrameworks/FitnessCanvasUI.framework/FitnessCanvasUI](DYLIBS/FitnessCanvasUI.md)
- [/System/Library/PrivateFrameworks/FitnessCoaching.framework/FitnessCoaching](DYLIBS/FitnessCoaching.md)
- [/System/Library/PrivateFrameworks/FitnessCoachingServices.framework/FitnessCoachingServices](DYLIBS/FitnessCoachingServices.md)
- [/System/Library/PrivateFrameworks/FitnessFiltering.framework/FitnessFiltering](DYLIBS/FitnessFiltering.md)
- [/System/Library/PrivateFrameworks/FitnessLibrary.framework/FitnessLibrary](DYLIBS/FitnessLibrary.md)
- [/System/Library/PrivateFrameworks/FitnessUI.framework/FitnessUI](DYLIBS/FitnessUI.md)
- [/System/Library/PrivateFrameworks/FocusSettingsUI.framework/FocusSettingsUI](DYLIBS/FocusSettingsUI.md)
- [/System/Library/PrivateFrameworks/FontServices.framework/libFontParser.dylib](DYLIBS/libFontParser.dylib.md)
- [/System/Library/PrivateFrameworks/FusionTracker.framework/FusionTracker](DYLIBS/FusionTracker.md)
- [/System/Library/PrivateFrameworks/GRDBInternal.framework/GRDBInternal](DYLIBS/GRDBInternal.md)
- [/System/Library/PrivateFrameworks/GameCenterFoundation.framework/GameCenterFoundation](DYLIBS/GameCenterFoundation.md)
- [/System/Library/PrivateFrameworks/GameCenterUI.framework/GameCenterUI](DYLIBS/GameCenterUI.md)
- [/System/Library/PrivateFrameworks/GamePolicy.framework/GamePolicy](DYLIBS/GamePolicy.md)
- [/System/Library/PrivateFrameworks/GenerativeExperiencesRuntime.framework/GenerativeExperiencesRuntime](DYLIBS/GenerativeExperiencesRuntime.md)
- [/System/Library/PrivateFrameworks/GenerativeFunctionsFoundation.framework/GenerativeFunctionsFoundation](DYLIBS/GenerativeFunctionsFoundation.md)
- [/System/Library/PrivateFrameworks/GenerativeFunctionsInstrumentation.framework/GenerativeFunctionsInstrumentation](DYLIBS/GenerativeFunctionsInstrumentation.md)
- [/System/Library/PrivateFrameworks/GenerativeModelsFoundation.framework/GenerativeModelsFoundation](DYLIBS/GenerativeModelsFoundation.md)
- [/System/Library/PrivateFrameworks/GroupKitCrypto.framework/GroupKitCrypto](DYLIBS/GroupKitCrypto.md)
- [/System/Library/PrivateFrameworks/Hands.framework/Hands](DYLIBS/Hands.md)
- [/System/Library/PrivateFrameworks/HangTracer.framework/HangTracer](DYLIBS/HangTracer.md)
- [/System/Library/PrivateFrameworks/HeadGestures.framework/HeadGestures](DYLIBS/HeadGestures.md)
- [/System/Library/PrivateFrameworks/HeadphoneConfigs.framework/HeadphoneConfigs](DYLIBS/HeadphoneConfigs.md)
- [/System/Library/PrivateFrameworks/HealthBalanceDaemon.framework/HealthBalanceDaemon](DYLIBS/HealthBalanceDaemon.md)
- [/System/Library/PrivateFrameworks/HealthBalanceUI.framework/HealthBalanceUI](DYLIBS/HealthBalanceUI.md)
- [/System/Library/PrivateFrameworks/HealthExperienceUI.framework/HealthExperienceUI](DYLIBS/HealthExperienceUI.md)
- [/System/Library/PrivateFrameworks/HealthExposureNotificationUI.framework/HealthExposureNotificationUI](DYLIBS/HealthExposureNotificationUI.md)
- [/System/Library/PrivateFrameworks/HealthMedicationsUI.framework/HealthMedicationsUI](DYLIBS/HealthMedicationsUI.md)
- [/System/Library/PrivateFrameworks/HealthMenstrualCyclesDaemon.framework/HealthMenstrualCyclesDaemon](DYLIBS/HealthMenstrualCyclesDaemon.md)
- [/System/Library/PrivateFrameworks/HealthMobilityUI.framework/HealthMobilityUI](DYLIBS/HealthMobilityUI.md)
- [/System/Library/PrivateFrameworks/HealthPluginHost.framework/HealthPluginHost](DYLIBS/HealthPluginHost.md)
- [/System/Library/PrivateFrameworks/HealthRecordsDaemon.framework/HealthRecordsDaemon](DYLIBS/HealthRecordsDaemon.md)
- [/System/Library/PrivateFrameworks/HealthUI.framework/HealthUI](DYLIBS/HealthUI.md)
- [/System/Library/PrivateFrameworks/HealthVisualization.framework/HealthVisualization](DYLIBS/HealthVisualization.md)
- [/System/Library/PrivateFrameworks/HearingModeService.framework/HearingModeService](DYLIBS/HearingModeService.md)
- [/System/Library/PrivateFrameworks/HearingModeUI.framework/HearingModeUI](DYLIBS/HearingModeUI.md)
- [/System/Library/PrivateFrameworks/HearingTest.framework/HearingTest](DYLIBS/HearingTest.md)
- [/System/Library/PrivateFrameworks/HelpKit.framework/HelpKit](DYLIBS/HelpKit.md)
- [/System/Library/PrivateFrameworks/Home.framework/Home](DYLIBS/Home.md)
- [/System/Library/PrivateFrameworks/HomeAccessoryControlUI.framework/HomeAccessoryControlUI](DYLIBS/HomeAccessoryControlUI.md)
- [/System/Library/PrivateFrameworks/HomeAutomationInternal.framework/HomeAutomationInternal](DYLIBS/HomeAutomationInternal.md)
- [/System/Library/PrivateFrameworks/HomeEnergyDaemon.framework/HomeEnergyDaemon](DYLIBS/HomeEnergyDaemon.md)
- [/System/Library/PrivateFrameworks/HomeEnergyUI.framework/HomeEnergyUI](DYLIBS/HomeEnergyUI.md)
- [/System/Library/PrivateFrameworks/HomeKitCore.framework/HomeKitCore](DYLIBS/HomeKitCore.md)
- [/System/Library/PrivateFrameworks/HomeKitDaemon.framework/HomeKitDaemon](DYLIBS/HomeKitDaemon.md)
- [/System/Library/PrivateFrameworks/HomeKitDaemonLegacy.framework/HomeKitDaemonLegacy](DYLIBS/HomeKitDaemonLegacy.md)
- [/System/Library/PrivateFrameworks/HomeKitEvents.framework/HomeKitEvents](DYLIBS/HomeKitEvents.md)
- [/System/Library/PrivateFrameworks/HomePlatformSettingsUI.framework/HomePlatformSettingsUI](DYLIBS/HomePlatformSettingsUI.md)
- [/System/Library/PrivateFrameworks/HomePodSettings.framework/HomePodSettings](DYLIBS/HomePodSettings.md)
- [/System/Library/PrivateFrameworks/HomeUI.framework/HomeUI](DYLIBS/HomeUI.md)
- [/System/Library/PrivateFrameworks/HomeUtilityServices.framework/HomeUtilityServices](DYLIBS/HomeUtilityServices.md)
- [/System/Library/PrivateFrameworks/HoverTextUI.framework/HoverTextUI](DYLIBS/HoverTextUI.md)
- [/System/Library/PrivateFrameworks/Human.framework/Human](DYLIBS/Human.md)
- [/System/Library/PrivateFrameworks/IDS.framework/IDS](DYLIBS/IDS.md)
- [/System/Library/PrivateFrameworks/IMCore.framework/IMCore](DYLIBS/IMCore.md)
- [/System/Library/PrivateFrameworks/IMSharedUtilities.framework/IMSharedUtilities](DYLIBS/IMSharedUtilities.md)
- [/System/Library/PrivateFrameworks/IO80211.framework/IO80211](DYLIBS/IO80211.md)
- [/System/Library/PrivateFrameworks/IPTelephony.framework/Support/libIPTelephony.dylib](DYLIBS/libIPTelephony.dylib.md)
- [/System/Library/PrivateFrameworks/IntelligenceEngine.framework/IntelligenceEngine](DYLIBS/IntelligenceEngine.md)
- [/System/Library/PrivateFrameworks/IntelligenceFlowPlannerRuntime.framework/IntelligenceFlowPlannerRuntime](DYLIBS/IntelligenceFlowPlannerRuntime.md)
- [/System/Library/PrivateFrameworks/IntelligenceFlowRuntime.framework/IntelligenceFlowRuntime](DYLIBS/IntelligenceFlowRuntime.md)
- [/System/Library/PrivateFrameworks/IntelligencePlatform.framework/IntelligencePlatform](DYLIBS/IntelligencePlatform.md)
- [/System/Library/PrivateFrameworks/IntelligencePlatformCore.framework/IntelligencePlatformCore](DYLIBS/IntelligencePlatformCore.md)
- [/System/Library/PrivateFrameworks/IntelligencePlatformLibrary.framework/IntelligencePlatformLibrary](DYLIBS/IntelligencePlatformLibrary.md)
- [/System/Library/PrivateFrameworks/IntelligentTrackingCore.framework/IntelligentTrackingCore](DYLIBS/IntelligentTrackingCore.md)
- [/System/Library/PrivateFrameworks/JetEngine.framework/JetEngine](DYLIBS/JetEngine.md)
- [/System/Library/PrivateFrameworks/JetUI.framework/JetUI](DYLIBS/JetUI.md)
- [/System/Library/PrivateFrameworks/KeyboardArbiter.framework/KeyboardArbiter](DYLIBS/KeyboardArbiter.md)
- [/System/Library/PrivateFrameworks/KeyboardSettings.framework/KeyboardSettings](DYLIBS/KeyboardSettings.md)
- [/System/Library/PrivateFrameworks/KeyboardSettingsFeedback.framework/KeyboardSettingsFeedback](DYLIBS/KeyboardSettingsFeedback.md)
- [/System/Library/PrivateFrameworks/KeychainCircle.framework/KeychainCircle](DYLIBS/KeychainCircle.md)
- [/System/Library/PrivateFrameworks/LiftUI.framework/LiftUI](DYLIBS/LiftUI.md)
- [/System/Library/PrivateFrameworks/LighthouseDataProcessor.framework/LighthouseDataProcessor](DYLIBS/LighthouseDataProcessor.md)
- [/System/Library/PrivateFrameworks/LinkMetadata.framework/LinkMetadata](DYLIBS/LinkMetadata.md)
- [/System/Library/PrivateFrameworks/LiveExecutionResultsProbe.framework/LiveExecutionResultsProbe](DYLIBS/LiveExecutionResultsProbe.md)
- [/System/Library/PrivateFrameworks/LocalAuthenticationCore.framework/LocalAuthenticationCore](DYLIBS/LocalAuthenticationCore.md)
- [/System/Library/PrivateFrameworks/MLModelSpecification.framework/MLModelSpecification](DYLIBS/MLModelSpecification.md)
- [/System/Library/PrivateFrameworks/MTLToolsDeviceSupport.framework/MTLToolsDeviceSupport](DYLIBS/MTLToolsDeviceSupport.md)
- [/System/Library/PrivateFrameworks/MagnifierSupport.framework/MagnifierSupport](DYLIBS/MagnifierSupport.md)
- [/System/Library/PrivateFrameworks/MailUI.framework/MailUI](DYLIBS/MailUI.md)
- [/System/Library/PrivateFrameworks/MapsSync.framework/MapsSync](DYLIBS/MapsSync.md)
- [/System/Library/PrivateFrameworks/MapsUI.framework/MapsUI](DYLIBS/MapsUI.md)
- [/System/Library/PrivateFrameworks/MeasureFoundation.framework/MeasureFoundation](DYLIBS/MeasureFoundation.md)
- [/System/Library/PrivateFrameworks/MediaControlSender.framework/MediaControlSender](DYLIBS/MediaControlSender.md)
- [/System/Library/PrivateFrameworks/MediaControls.framework/MediaControls](DYLIBS/MediaControls.md)
- [/System/Library/PrivateFrameworks/MediaCoreUI.framework/MediaCoreUI](DYLIBS/MediaCoreUI.md)
- [/System/Library/PrivateFrameworks/MediaPlaybackCore.framework/MediaPlaybackCore](DYLIBS/MediaPlaybackCore.md)
- [/System/Library/PrivateFrameworks/MentalHealthUI.framework/MentalHealthUI](DYLIBS/MentalHealthUI.md)
- [/System/Library/PrivateFrameworks/Message.framework/Message](DYLIBS/Message.md)
- [/System/Library/PrivateFrameworks/MessageProtection.framework/MessageProtection](DYLIBS/MessageProtection.md)
- [/System/Library/PrivateFrameworks/MessagesCloudSync.framework/MessagesCloudSync](DYLIBS/MessagesCloudSync.md)
- [/System/Library/PrivateFrameworks/MetricsFramework.framework/MetricsFramework](DYLIBS/MetricsFramework.md)
- [/System/Library/PrivateFrameworks/MobileBackup.framework/MobileBackup](DYLIBS/MobileBackup.md)
- [/System/Library/PrivateFrameworks/MobileSafari.framework/MobileSafari](DYLIBS/MobileSafari.md)
- [/System/Library/PrivateFrameworks/MobileSpotlightIndex.framework/MobileSpotlightIndex](DYLIBS/MobileSpotlightIndex.md)
- [/System/Library/PrivateFrameworks/MobileStoreUI.framework/MobileStoreUI](DYLIBS/MobileStoreUI.md)
- [/System/Library/PrivateFrameworks/MobileTimerSupport.framework/MobileTimerSupport](DYLIBS/MobileTimerSupport.md)
- [/System/Library/PrivateFrameworks/ModelManagerServices.framework/ModelManagerServices](DYLIBS/ModelManagerServices.md)
- [/System/Library/PrivateFrameworks/Moments.framework/Moments](DYLIBS/Moments.md)
- [/System/Library/PrivateFrameworks/MomentsOnboardingAndSettings.framework/MomentsOnboardingAndSettings](DYLIBS/MomentsOnboardingAndSettings.md)
- [/System/Library/PrivateFrameworks/Morpheus.framework/Morpheus](DYLIBS/Morpheus.md)
- [/System/Library/PrivateFrameworks/MusicKitInternal.framework/MusicKitInternal](DYLIBS/MusicKitInternal.md)
- [/System/Library/PrivateFrameworks/MusicUI.framework/MusicUI](DYLIBS/MusicUI.md)
- [/System/Library/PrivateFrameworks/NanoWeatherKitUICompanion.framework/NanoWeatherKitUICompanion](DYLIBS/NanoWeatherKitUICompanion.md)
- [/System/Library/PrivateFrameworks/NetworkServiceProxy.framework/NetworkServiceProxy](DYLIBS/NetworkServiceProxy.md)
- [/System/Library/PrivateFrameworks/NeuralNetworks.framework/NeuralNetworks](DYLIBS/NeuralNetworks.md)
- [/System/Library/PrivateFrameworks/NewDeviceOutreach.framework/NewDeviceOutreach](DYLIBS/NewDeviceOutreach.md)
- [/System/Library/PrivateFrameworks/NewsArticles.framework/NewsArticles](DYLIBS/NewsArticles.md)
- [/System/Library/PrivateFrameworks/NewsFeed.framework/NewsFeed](DYLIBS/NewsFeed.md)
- [/System/Library/PrivateFrameworks/NewsPersonalization.framework/NewsPersonalization](DYLIBS/NewsPersonalization.md)
- [/System/Library/PrivateFrameworks/NewsSubscription.framework/NewsSubscription](DYLIBS/NewsSubscription.md)
- [/System/Library/PrivateFrameworks/NewsUI2.framework/NewsUI2](DYLIBS/NewsUI2.md)
- [/System/Library/PrivateFrameworks/NexusDaemon.framework/NexusDaemon](DYLIBS/NexusDaemon.md)
- [/System/Library/PrivateFrameworks/NightingaleTraining.framework/NightingaleTraining](DYLIBS/NightingaleTraining.md)
- [/System/Library/PrivateFrameworks/NotesEditor.framework/NotesEditor](DYLIBS/NotesEditor.md)
- [/System/Library/PrivateFrameworks/NotesShared.framework/NotesShared](DYLIBS/NotesShared.md)
- [/System/Library/PrivateFrameworks/NotesUI.framework/NotesUI](DYLIBS/NotesUI.md)
- [/System/Library/PrivateFrameworks/ODCurareEvaluationAndReporting.framework/ODCurareEvaluationAndReporting](DYLIBS/ODCurareEvaluationAndReporting.md)
- [/System/Library/PrivateFrameworks/OSAnalytics.framework/OSAnalytics](DYLIBS/OSAnalytics.md)
- [/System/Library/PrivateFrameworks/OmniSearch.framework/OmniSearch](DYLIBS/OmniSearch.md)
- [/System/Library/PrivateFrameworks/OnBoardingKit.framework/OnBoardingKit](DYLIBS/OnBoardingKit.md)
- [/System/Library/PrivateFrameworks/PairedDeviceRegistry.framework/PairedDeviceRegistry](DYLIBS/PairedDeviceRegistry.md)
- [/System/Library/PrivateFrameworks/PaperBoardUI.framework/PaperBoardUI](DYLIBS/PaperBoardUI.md)
- [/System/Library/PrivateFrameworks/PaperKit.framework/PaperKit](DYLIBS/PaperKit.md)
- [/System/Library/PrivateFrameworks/PassKitCore.framework/PassKitCore](DYLIBS/PassKitCore.md)
- [/System/Library/PrivateFrameworks/PassKitUI.framework/PassKitUI](DYLIBS/PassKitUI.md)
- [/System/Library/PrivateFrameworks/PasswordManagerUI.framework/PasswordManagerUI](DYLIBS/PasswordManagerUI.md)
- [/System/Library/PrivateFrameworks/PegasusConfiguration.framework/PegasusConfiguration](DYLIBS/PegasusConfiguration.md)
- [/System/Library/PrivateFrameworks/People.framework/People](DYLIBS/People.md)
- [/System/Library/PrivateFrameworks/PeopleUI.framework/PeopleUI](DYLIBS/PeopleUI.md)
- [/System/Library/PrivateFrameworks/PersonalizedSensing.framework/PersonalizedSensing](DYLIBS/PersonalizedSensing.md)
- [/System/Library/PrivateFrameworks/PhotoAnalysis.framework/PhotoAnalysis](DYLIBS/PhotoAnalysis.md)
- [/System/Library/PrivateFrameworks/PhotoLibraryServices.framework/PhotoLibraryServices](DYLIBS/PhotoLibraryServices.md)
- [/System/Library/PrivateFrameworks/PhotosFace.framework/PhotosFace](DYLIBS/PhotosFace.md)
- [/System/Library/PrivateFrameworks/PhotosGraph.framework/PhotosGraph](DYLIBS/PhotosGraph.md)
- [/System/Library/PrivateFrameworks/PhotosIntelligence.framework/PhotosIntelligence](DYLIBS/PhotosIntelligence.md)
- [/System/Library/PrivateFrameworks/PhotosSwiftUICore.framework/PhotosSwiftUICore](DYLIBS/PhotosSwiftUICore.md)
- [/System/Library/PrivateFrameworks/PhotosUICore.framework/PhotosUICore](DYLIBS/PhotosUICore.md)
- [/System/Library/PrivateFrameworks/PhotosUIPrivate.framework/PhotosUIPrivate](DYLIBS/PhotosUIPrivate.md)
- [/System/Library/PrivateFrameworks/PodcastsFoundation.framework/PodcastsFoundation](DYLIBS/PodcastsFoundation.md)
- [/System/Library/PrivateFrameworks/PodcastsUI.framework/PodcastsUI](DYLIBS/PodcastsUI.md)
- [/System/Library/PrivateFrameworks/PoirotBlocks.framework/PoirotBlocks](DYLIBS/PoirotBlocks.md)
- [/System/Library/PrivateFrameworks/PoirotSchematizer.framework/PoirotSchematizer](DYLIBS/PoirotSchematizer.md)
- [/System/Library/PrivateFrameworks/PoirotUDFs.framework/PoirotUDFs](DYLIBS/PoirotUDFs.md)
- [/System/Library/PrivateFrameworks/PosterBoard.framework/PosterBoard](DYLIBS/PosterBoard.md)
- [/System/Library/PrivateFrameworks/PosterBoardUIServices.framework/PosterBoardUIServices](DYLIBS/PosterBoardUIServices.md)
- [/System/Library/PrivateFrameworks/PosterFoundation.framework/PosterFoundation](DYLIBS/PosterFoundation.md)
- [/System/Library/PrivateFrameworks/PosterKit.framework/PosterKit](DYLIBS/PosterKit.md)
- [/System/Library/PrivateFrameworks/PowerlogCore.framework/PowerlogCore](DYLIBS/PowerlogCore.md)
- [/System/Library/PrivateFrameworks/Preferences.framework/Preferences](DYLIBS/Preferences.md)
- [/System/Library/PrivateFrameworks/PreviewShellKit.framework/PreviewShellKit](DYLIBS/PreviewShellKit.md)
- [/System/Library/PrivateFrameworks/PreviewsFoundationOS.framework/PreviewsFoundationOS](DYLIBS/PreviewsFoundationOS.md)
- [/System/Library/PrivateFrameworks/PreviewsInjection.framework/PreviewsInjection](DYLIBS/PreviewsInjection.md)
- [/System/Library/PrivateFrameworks/PreviewsMessagingOS.framework/PreviewsMessagingOS](DYLIBS/PreviewsMessagingOS.md)
- [/System/Library/PrivateFrameworks/PreviewsServicesUI.framework/PreviewsServicesUI](DYLIBS/PreviewsServicesUI.md)
- [/System/Library/PrivateFrameworks/PrivateFederatedLearning.framework/PrivateFederatedLearning](DYLIBS/PrivateFederatedLearning.md)
- [/System/Library/PrivateFrameworks/PrivateMLClient.framework/PrivateMLClient](DYLIBS/PrivateMLClient.md)
- [/System/Library/PrivateFrameworks/ProactiveSummarization.framework/ProactiveSummarization](DYLIBS/ProactiveSummarization.md)
- [/System/Library/PrivateFrameworks/ProductKit.framework/ProductKit](DYLIBS/ProductKit.md)
- [/System/Library/PrivateFrameworks/ProtectedCloudStorage.framework/ProtectedCloudStorage](DYLIBS/ProtectedCloudStorage.md)
- [/System/Library/PrivateFrameworks/ProximityAppleIDSetup.framework/ProximityAppleIDSetup](DYLIBS/ProximityAppleIDSetup.md)
- [/System/Library/PrivateFrameworks/ProximityAppleIDSetupUI.framework/ProximityAppleIDSetupUI](DYLIBS/ProximityAppleIDSetupUI.md)
- [/System/Library/PrivateFrameworks/ProximityReaderDaemon.framework/ProximityReaderDaemon](DYLIBS/ProximityReaderDaemon.md)
- [/System/Library/PrivateFrameworks/QOSToolkit.framework/QOSToolkit](DYLIBS/QOSToolkit.md)
- [/System/Library/PrivateFrameworks/RealityKitInspection.framework/RealityKitInspection](DYLIBS/RealityKitInspection.md)
- [/System/Library/PrivateFrameworks/ReminderKitInternal.framework/ReminderKitInternal](DYLIBS/ReminderKitInternal.md)
- [/System/Library/PrivateFrameworks/RemindersUICore.framework/RemindersUICore](DYLIBS/RemindersUICore.md)
- [/System/Library/PrivateFrameworks/RemotePairingDevice.framework/RemotePairingDevice](DYLIBS/RemotePairingDevice.md)
- [/System/Library/PrivateFrameworks/RemoteUI.framework/RemoteUI](DYLIBS/RemoteUI.md)
- [/System/Library/PrivateFrameworks/RenderBox.framework/RenderBox](DYLIBS/RenderBox.md)
- [/System/Library/PrivateFrameworks/ReplicatorCore.framework/ReplicatorCore](DYLIBS/ReplicatorCore.md)
- [/System/Library/PrivateFrameworks/ReplicatorEngine.framework/ReplicatorEngine](DYLIBS/ReplicatorEngine.md)
- [/System/Library/PrivateFrameworks/ReplicatorServices.framework/ReplicatorServices](DYLIBS/ReplicatorServices.md)
- [/System/Library/PrivateFrameworks/ReportingPlugin.framework/ReportingPlugin](DYLIBS/ReportingPlugin.md)
- [/System/Library/PrivateFrameworks/RuntimeInternal.framework/RuntimeInternal](DYLIBS/RuntimeInternal.md)
- [/System/Library/PrivateFrameworks/SFSymbols.framework/SFSymbols](DYLIBS/SFSymbols.md)
- [/System/Library/PrivateFrameworks/SafetyMonitorUI.framework/SafetyMonitorUI](DYLIBS/SafetyMonitorUI.md)
- [/System/Library/PrivateFrameworks/ScreenReaderOutput.framework/ScreenReaderOutput](DYLIBS/ScreenReaderOutput.md)
- [/System/Library/PrivateFrameworks/ScreenSharingKit.framework/ScreenSharingKit](DYLIBS/ScreenSharingKit.md)
- [/System/Library/PrivateFrameworks/ScreenTimeSettingsUI.framework/ScreenTimeSettingsUI](DYLIBS/ScreenTimeSettingsUI.md)
- [/System/Library/PrivateFrameworks/ScreenTimeUICore.framework/ScreenTimeUICore](DYLIBS/ScreenTimeUICore.md)
- [/System/Library/PrivateFrameworks/SearchAssets.framework/SearchAssets](DYLIBS/SearchAssets.md)
- [/System/Library/PrivateFrameworks/SearchOnDeviceAnalytics.framework/SearchOnDeviceAnalytics](DYLIBS/SearchOnDeviceAnalytics.md)
- [/System/Library/PrivateFrameworks/SearchUI.framework/SearchUI](DYLIBS/SearchUI.md)
- [/System/Library/PrivateFrameworks/SensingAlgsService.framework/SensingAlgsService](DYLIBS/SensingAlgsService.md)
- [/System/Library/PrivateFrameworks/SensingAlgsTouchButtonHost.framework/SensingAlgsTouchButtonHost](DYLIBS/SensingAlgsTouchButtonHost.md)
- [/System/Library/PrivateFrameworks/Sentry.framework/Sentry](DYLIBS/Sentry.md)
- [/System/Library/PrivateFrameworks/SessionCore.framework/SessionCore](DYLIBS/SessionCore.md)
- [/System/Library/PrivateFrameworks/Settings.framework/Settings](DYLIBS/Settings.md)
- [/System/Library/PrivateFrameworks/Settings/PrivacySettingsUI.framework/PrivacySettingsUI](DYLIBS/PrivacySettingsUI.md)
- [/System/Library/PrivateFrameworks/SetupAssistant.framework/SetupAssistant](DYLIBS/SetupAssistant.md)
- [/System/Library/PrivateFrameworks/SetupAssistantSupportUI.framework/SetupAssistantSupportUI](DYLIBS/SetupAssistantSupportUI.md)
- [/System/Library/PrivateFrameworks/SeymourMedia.framework/SeymourMedia](DYLIBS/SeymourMedia.md)
- [/System/Library/PrivateFrameworks/SeymourServices.framework/SeymourServices](DYLIBS/SeymourServices.md)
- [/System/Library/PrivateFrameworks/SeymourUI.framework/SeymourUI](DYLIBS/SeymourUI.md)
- [/System/Library/PrivateFrameworks/ShaderGraph.framework/ShaderGraph](DYLIBS/ShaderGraph.md)
- [/System/Library/PrivateFrameworks/Sharing.framework/Sharing](DYLIBS/Sharing.md)
- [/System/Library/PrivateFrameworks/ShazamEvents.framework/ShazamEvents](DYLIBS/ShazamEvents.md)
- [/System/Library/PrivateFrameworks/ShellSceneKit.framework/ShellSceneKit](DYLIBS/ShellSceneKit.md)
- [/System/Library/PrivateFrameworks/ShimGameServices.framework/ShimGameServices](DYLIBS/ShimGameServices.md)
- [/System/Library/PrivateFrameworks/SiriAnalytics.framework/SiriAnalytics](DYLIBS/SiriAnalytics.md)
- [/System/Library/PrivateFrameworks/SiriAppLaunchIntents.framework/SiriAppLaunchIntents](DYLIBS/SiriAppLaunchIntents.md)
- [/System/Library/PrivateFrameworks/SiriAudioSupport.framework/SiriAudioSupport](DYLIBS/SiriAudioSupport.md)
- [/System/Library/PrivateFrameworks/SiriAutoComplete.framework/SiriAutoComplete](DYLIBS/SiriAutoComplete.md)
- [/System/Library/PrivateFrameworks/SiriCalendarIntents.framework/SiriCalendarIntents](DYLIBS/SiriCalendarIntents.md)
- [/System/Library/PrivateFrameworks/SiriCalendarUI.framework/SiriCalendarUI](DYLIBS/SiriCalendarUI.md)
- [/System/Library/PrivateFrameworks/SiriCam.framework/SiriCam](DYLIBS/SiriCam.md)
- [/System/Library/PrivateFrameworks/SiriContactsIntents.framework/SiriContactsIntents](DYLIBS/SiriContactsIntents.md)
- [/System/Library/PrivateFrameworks/SiriExpanseInternal.framework/SiriExpanseInternal](DYLIBS/SiriExpanseInternal.md)
- [/System/Library/PrivateFrameworks/SiriExpanseInternalUI.framework/SiriExpanseInternalUI](DYLIBS/SiriExpanseInternalUI.md)
- [/System/Library/PrivateFrameworks/SiriFindMy.framework/SiriFindMy](DYLIBS/SiriFindMy.md)
- [/System/Library/PrivateFrameworks/SiriGestureBridge.framework/SiriGestureBridge](DYLIBS/SiriGestureBridge.md)
- [/System/Library/PrivateFrameworks/SiriIdentityInternal.framework/SiriIdentityInternal](DYLIBS/SiriIdentityInternal.md)
- [/System/Library/PrivateFrameworks/SiriInCall.framework/SiriInCall](DYLIBS/SiriInCall.md)
- [/System/Library/PrivateFrameworks/SiriInference.framework/SiriInference](DYLIBS/SiriInference.md)
- [/System/Library/PrivateFrameworks/SiriInformationSearch.framework/SiriInformationSearch](DYLIBS/SiriInformationSearch.md)
- [/System/Library/PrivateFrameworks/SiriKitFlow.framework/SiriKitFlow](DYLIBS/SiriKitFlow.md)
- [/System/Library/PrivateFrameworks/SiriKitRuntime.framework/SiriKitRuntime](DYLIBS/SiriKitRuntime.md)
- [/System/Library/PrivateFrameworks/SiriMailInternal.framework/SiriMailInternal](DYLIBS/SiriMailInternal.md)
- [/System/Library/PrivateFrameworks/SiriMailUI.framework/SiriMailUI](DYLIBS/SiriMailUI.md)
- [/System/Library/PrivateFrameworks/SiriMessageBus.framework/SiriMessageBus](DYLIBS/SiriMessageBus.md)
- [/System/Library/PrivateFrameworks/SiriMessageTypes.framework/SiriMessageTypes](DYLIBS/SiriMessageTypes.md)
- [/System/Library/PrivateFrameworks/SiriMessagesFlow.framework/SiriMessagesFlow](DYLIBS/SiriMessagesFlow.md)
- [/System/Library/PrivateFrameworks/SiriMessagesUI.framework/SiriMessagesUI](DYLIBS/SiriMessagesUI.md)
- [/System/Library/PrivateFrameworks/SiriNaturalLanguageGeneration.framework/SiriNaturalLanguageGeneration](DYLIBS/SiriNaturalLanguageGeneration.md)
- [/System/Library/PrivateFrameworks/SiriNetwork.framework/SiriNetwork](DYLIBS/SiriNetwork.md)
- [/System/Library/PrivateFrameworks/SiriNotebook.framework/SiriNotebook](DYLIBS/SiriNotebook.md)
- [/System/Library/PrivateFrameworks/SiriNotebookUI.framework/SiriNotebookUI](DYLIBS/SiriNotebookUI.md)
- [/System/Library/PrivateFrameworks/SiriNotificationsIntents.framework/SiriNotificationsIntents](DYLIBS/SiriNotificationsIntents.md)
- [/System/Library/PrivateFrameworks/SiriOntology.framework/SiriOntology](DYLIBS/SiriOntology.md)
- [/System/Library/PrivateFrameworks/SiriPaymentsIntents.framework/SiriPaymentsIntents](DYLIBS/SiriPaymentsIntents.md)
- [/System/Library/PrivateFrameworks/SiriPlaybackControlIntents.framework/SiriPlaybackControlIntents](DYLIBS/SiriPlaybackControlIntents.md)
- [/System/Library/PrivateFrameworks/SiriPrivateLearningAnalytics.framework/SiriPrivateLearningAnalytics](DYLIBS/SiriPrivateLearningAnalytics.md)
- [/System/Library/PrivateFrameworks/SiriPrivateLearningInference.framework/SiriPrivateLearningInference](DYLIBS/SiriPrivateLearningInference.md)
- [/System/Library/PrivateFrameworks/SiriRemembers.framework/SiriRemembers](DYLIBS/SiriRemembers.md)
- [/System/Library/PrivateFrameworks/SiriSettingsIntents.framework/SiriSettingsIntents](DYLIBS/SiriSettingsIntents.md)
- [/System/Library/PrivateFrameworks/SiriSetup.framework/SiriSetup](DYLIBS/SiriSetup.md)
- [/System/Library/PrivateFrameworks/SiriSharedUI.framework/SiriSharedUI](DYLIBS/SiriSharedUI.md)
- [/System/Library/PrivateFrameworks/SiriSignals.framework/SiriSignals](DYLIBS/SiriSignals.md)
- [/System/Library/PrivateFrameworks/SiriSuggestions.framework/SiriSuggestions](DYLIBS/SiriSuggestions.md)
- [/System/Library/PrivateFrameworks/SiriSuggestionsAPI.framework/SiriSuggestionsAPI](DYLIBS/SiriSuggestionsAPI.md)
- [/System/Library/PrivateFrameworks/SiriSuggestionsIntelligence.framework/SiriSuggestionsIntelligence](DYLIBS/SiriSuggestionsIntelligence.md)
- [/System/Library/PrivateFrameworks/SiriTTSService.framework/SiriTTSService](DYLIBS/SiriTTSService.md)
- [/System/Library/PrivateFrameworks/SiriTimeTimerInternal.framework/SiriTimeTimerInternal](DYLIBS/SiriTimeTimerInternal.md)
- [/System/Library/PrivateFrameworks/SiriTranslationIntents.framework/SiriTranslationIntents](DYLIBS/SiriTranslationIntents.md)
- [/System/Library/PrivateFrameworks/SiriVideoIntents.framework/SiriVideoIntents](DYLIBS/SiriVideoIntents.md)
- [/System/Library/PrivateFrameworks/SiriVideoUIFramework.framework/SiriVideoUIFramework](DYLIBS/SiriVideoUIFramework.md)
- [/System/Library/PrivateFrameworks/SleepHealthUI.framework/SleepHealthUI](DYLIBS/SleepHealthUI.md)
- [/System/Library/PrivateFrameworks/SleepWidgetUI.framework/SleepWidgetUI](DYLIBS/SleepWidgetUI.md)
- [/System/Library/PrivateFrameworks/SnippetUI.framework/SnippetUI](DYLIBS/SnippetUI.md)
- [/System/Library/PrivateFrameworks/SoftwareUpdateServices.framework/SoftwareUpdateServices](DYLIBS/SoftwareUpdateServices.md)
- [/System/Library/PrivateFrameworks/SonicFoundation.framework/SonicFoundation](DYLIBS/SonicFoundation.md)
- [/System/Library/PrivateFrameworks/SonicKit.framework/SonicKit](DYLIBS/SonicKit.md)
- [/System/Library/PrivateFrameworks/SpotlightDaemon.framework/SpotlightDaemon](DYLIBS/SpotlightDaemon.md)
- [/System/Library/PrivateFrameworks/SpotlightServices.framework/SpotlightServices](DYLIBS/SpotlightServices.md)
- [/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard](DYLIBS/SpringBoard.md)
- [/System/Library/PrivateFrameworks/Stickers.framework/Stickers](DYLIBS/Stickers.md)
- [/System/Library/PrivateFrameworks/StocksCore.framework/StocksCore](DYLIBS/StocksCore.md)
- [/System/Library/PrivateFrameworks/StocksUI.framework/StocksUI](DYLIBS/StocksUI.md)
- [/System/Library/PrivateFrameworks/StorageKit.framework/StorageKit](DYLIBS/StorageKit.md)
- [/System/Library/PrivateFrameworks/StorageUI.framework/StorageUI](DYLIBS/StorageUI.md)
- [/System/Library/PrivateFrameworks/StoreServices.framework/StoreServices](DYLIBS/StoreServices.md)
- [/System/Library/PrivateFrameworks/SummarizationKit.framework/SummarizationKit](DYLIBS/SummarizationKit.md)
- [/System/Library/PrivateFrameworks/SymptomDiagnosticReporter.framework/SymptomDiagnosticReporter](DYLIBS/SymptomDiagnosticReporter.md)
- [/System/Library/PrivateFrameworks/Symptoms.framework/Frameworks/SymptomEvaluator.framework/SymptomEvaluator](DYLIBS/SymptomEvaluator.md)
- [/System/Library/PrivateFrameworks/SyncedModels.framework/SyncedModels](DYLIBS/SyncedModels.md)
- [/System/Library/PrivateFrameworks/SystemStatus.framework/SystemStatus](DYLIBS/SystemStatus.md)
- [/System/Library/PrivateFrameworks/TVAppServices.framework/TVAppServices](DYLIBS/TVAppServices.md)
- [/System/Library/PrivateFrameworks/TVRemoteUI.framework/TVRemoteUI](DYLIBS/TVRemoteUI.md)
- [/System/Library/PrivateFrameworks/TeaFoundation.framework/TeaFoundation](DYLIBS/TeaFoundation.md)
- [/System/Library/PrivateFrameworks/TeaTemplate.framework/TeaTemplate](DYLIBS/TeaTemplate.md)
- [/System/Library/PrivateFrameworks/TeaUI.framework/TeaUI](DYLIBS/TeaUI.md)
- [/System/Library/PrivateFrameworks/TelephonyBlastDoorSupport.framework/TelephonyBlastDoorSupport](DYLIBS/TelephonyBlastDoorSupport.md)
- [/System/Library/PrivateFrameworks/TextFormattingUI.framework/TextFormattingUI](DYLIBS/TextFormattingUI.md)
- [/System/Library/PrivateFrameworks/TextInputCore.framework/TextInputCore](DYLIBS/TextInputCore.md)
- [/System/Library/PrivateFrameworks/TextInputUI.framework/TextInputUI](DYLIBS/TextInputUI.md)
- [/System/Library/PrivateFrameworks/TextToSpeech.framework/TextToSpeech](DYLIBS/TextToSpeech.md)
- [/System/Library/PrivateFrameworks/TextToSpeechVoiceBankingUI.framework/TextToSpeechVoiceBankingUI](DYLIBS/TextToSpeechVoiceBankingUI.md)
- [/System/Library/PrivateFrameworks/ThirdPartyApplicationSettings.framework/ThirdPartyApplicationSettings](DYLIBS/ThirdPartyApplicationSettings.md)
- [/System/Library/PrivateFrameworks/TipKitCore.framework/TipKitCore](DYLIBS/TipKitCore.md)
- [/System/Library/PrivateFrameworks/TipsCore.framework/TipsCore](DYLIBS/TipsCore.md)
- [/System/Library/PrivateFrameworks/TipsUI.framework/TipsUI](DYLIBS/TipsUI.md)
- [/System/Library/PrivateFrameworks/TokenGenerationInference.framework/TokenGenerationInference](DYLIBS/TokenGenerationInference.md)
- [/System/Library/PrivateFrameworks/ToolKit.framework/ToolKit](DYLIBS/ToolKit.md)
- [/System/Library/PrivateFrameworks/UIIntelligenceIntents.framework/UIIntelligenceIntents](DYLIBS/UIIntelligenceIntents.md)
- [/System/Library/PrivateFrameworks/UIIntelligenceSupportAgent.framework/UIIntelligenceSupportAgent](DYLIBS/UIIntelligenceSupportAgent.md)
- [/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore](DYLIBS/UIKitCore.md)
- [/System/Library/PrivateFrameworks/UIUnderstanding.framework/UIUnderstanding](DYLIBS/UIUnderstanding.md)
- [/System/Library/PrivateFrameworks/UniversalDrag.framework/UniversalDrag](DYLIBS/UniversalDrag.md)
- [/System/Library/PrivateFrameworks/UniversalHID.framework/UniversalHID](DYLIBS/UniversalHID.md)
- [/System/Library/PrivateFrameworks/UserNotificationsCore.framework/UserNotificationsCore](DYLIBS/UserNotificationsCore.md)
- [/System/Library/PrivateFrameworks/UserNotificationsKit.framework/UserNotificationsKit](DYLIBS/UserNotificationsKit.md)
- [/System/Library/PrivateFrameworks/UserNotificationsUIKit.framework/UserNotificationsUIKit](DYLIBS/UserNotificationsUIKit.md)
- [/System/Library/PrivateFrameworks/VFX.framework/VFX](DYLIBS/VFX.md)
- [/System/Library/PrivateFrameworks/VectorSearch.framework/VectorSearch](DYLIBS/VectorSearch.md)
- [/System/Library/PrivateFrameworks/VideoProcessing.framework/VideoProcessing](DYLIBS/VideoProcessing.md)
- [/System/Library/PrivateFrameworks/VideosUI.framework/VideosUI](DYLIBS/VideosUI.md)
- [/System/Library/PrivateFrameworks/VisionHWAccelerationServices.framework/VisionHWAccelerationServices](DYLIBS/VisionHWAccelerationServices.md)
- [/System/Library/PrivateFrameworks/VisionKitInternal.framework/VisionKitInternal](DYLIBS/VisionKitInternal.md)
- [/System/Library/PrivateFrameworks/VisualGeneration.framework/VisualGeneration](DYLIBS/VisualGeneration.md)
- [/System/Library/PrivateFrameworks/VisualIntelligence.framework/VisualIntelligence](DYLIBS/VisualIntelligence.md)
- [/System/Library/PrivateFrameworks/VisualUnderstanding.framework/VisualUnderstanding](DYLIBS/VisualUnderstanding.md)
- [/System/Library/PrivateFrameworks/VoiceActions.framework/VoiceActions](DYLIBS/VoiceActions.md)
- [/System/Library/PrivateFrameworks/VoiceShortcutClient.framework/VoiceShortcutClient](DYLIBS/VoiceShortcutClient.md)
- [/System/Library/PrivateFrameworks/VoiceShortcuts.framework/VoiceShortcuts](DYLIBS/VoiceShortcuts.md)
- [/System/Library/PrivateFrameworks/VoiceTrigger.framework/VoiceTrigger](DYLIBS/VoiceTrigger.md)
- [/System/Library/PrivateFrameworks/VoiceTriggerUI.framework/VoiceTriggerUI](DYLIBS/VoiceTriggerUI.md)
- [/System/Library/PrivateFrameworks/WPDaemon.framework/WPDaemon](DYLIBS/WPDaemon.md)
- [/System/Library/PrivateFrameworks/WatchFacesWallpaperSupport.framework/WatchFacesWallpaperSupport](DYLIBS/WatchFacesWallpaperSupport.md)
- [/System/Library/PrivateFrameworks/WeatherDaemon.framework/WeatherDaemon](DYLIBS/WeatherDaemon.md)
- [/System/Library/PrivateFrameworks/WeatherMaps.framework/WeatherMaps](DYLIBS/WeatherMaps.md)
- [/System/Library/PrivateFrameworks/WeatherUI.framework/WeatherUI](DYLIBS/WeatherUI.md)
- [/System/Library/PrivateFrameworks/WiFiKitUI.framework/WiFiKitUI](DYLIBS/WiFiKitUI.md)
- [/System/Library/PrivateFrameworks/WiFiPolicy.framework/WiFiPolicy](DYLIBS/WiFiPolicy.md)
- [/System/Library/PrivateFrameworks/WidgetRenderer.framework/WidgetRenderer](DYLIBS/WidgetRenderer.md)
- [/System/Library/PrivateFrameworks/WorkflowEditor.framework/WorkflowEditor](DYLIBS/WorkflowEditor.md)
- [/System/Library/PrivateFrameworks/WorkflowUI.framework/WorkflowUI](DYLIBS/WorkflowUI.md)
- [/System/Library/PrivateFrameworks/WorkflowUICore.framework/WorkflowUICore](DYLIBS/WorkflowUICore.md)
- [/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/WorkoutAnnouncements](DYLIBS/WorkoutAnnouncements.md)
- [/System/Library/PrivateFrameworks/WorkoutCore.framework/WorkoutCore](DYLIBS/WorkoutCore.md)
- [/System/Library/PrivateFrameworks/WorkoutUI.framework/WorkoutUI](DYLIBS/WorkoutUI.md)
- [/System/Library/PrivateFrameworks/_JetEngine_SwiftUI.framework/_JetEngine_SwiftUI](DYLIBS/_JetEngine_SwiftUI.md)
- [/System/Library/PrivateFrameworks/_MusicKitInternal_SwiftUI.framework/_MusicKitInternal_SwiftUI](DYLIBS/_MusicKitInternal_SwiftUI.md)
- [/System/Library/PrivateFrameworks/_SonicKit_MusicKit.framework/_SonicKit_MusicKit](DYLIBS/_SonicKit_MusicKit.md)
- [/System/Library/PrivateFrameworks/iCloudMailAccountUI.framework/iCloudMailAccountUI](DYLIBS/iCloudMailAccountUI.md)
- [/System/Library/PrivateFrameworks/iCloudQuotaUI.framework/iCloudQuotaUI](DYLIBS/iCloudQuotaUI.md)
- [/System/Library/VideoCodecs/VCPHEVC.videocodec](DYLIBS/VCPHEVC.videocodec.md)
- [/System/Library/VideoDecoders/AVD.videodecoder](DYLIBS/AVD.videodecoder.md)
- [/System/Library/VideoDecoders/H264H8.videodecoder](DYLIBS/H264H8.videodecoder.md)
- [/usr/lib/libATCommandStudioDynamic.dylib](DYLIBS/libATCommandStudioDynamic.dylib.md)
- [/usr/lib/libAppletTranslationLibrary.dylib](DYLIBS/libAppletTranslationLibrary.dylib.md)
- [/usr/lib/libAudioDSPCore.dylib](DYLIBS/libAudioDSPCore.dylib.md)
- [/usr/lib/libAudioIssueDetector.dylib](DYLIBS/libAudioIssueDetector.dylib.md)
- [/usr/lib/libAudioToolboxUtility.dylib](DYLIBS/libAudioToolboxUtility.dylib.md)
- [/usr/lib/libBBUpdaterDynamic.dylib](DYLIBS/libBBUpdaterDynamic.dylib.md)
- [/usr/lib/libBasebandCommandDriversARI.dylib](DYLIBS/libBasebandCommandDriversARI.dylib.md)
- [/usr/lib/libBasebandCommandDriversMIPC.dylib](DYLIBS/libBasebandCommandDriversMIPC.dylib.md)
- [/usr/lib/libBasebandCommandDriversQMI.dylib](DYLIBS/libBasebandCommandDriversQMI.dylib.md)
- [/usr/lib/libBasebandManager.dylib](DYLIBS/libBasebandManager.dylib.md)
- [/usr/lib/libBasebandManagerDAL.dylib](DYLIBS/libBasebandManagerDAL.dylib.md)
- [/usr/lib/libBasebandManagerICE.dylib](DYLIBS/libBasebandManagerICE.dylib.md)
- [/usr/lib/libETLDLFDynamic.dylib](DYLIBS/libETLDLFDynamic.dylib.md)
- [/usr/lib/libETLDLOADCoreDumpDynamic.dylib](DYLIBS/libETLDLOADCoreDumpDynamic.dylib.md)
- [/usr/lib/libETLDLOADDynamic.dylib](DYLIBS/libETLDLOADDynamic.dylib.md)
- [/usr/lib/libETLDMCDynamic.dylib](DYLIBS/libETLDMCDynamic.dylib.md)
- [/usr/lib/libETLDynamic.dylib](DYLIBS/libETLDynamic.dylib.md)
- [/usr/lib/libETLSAHDynamic.dylib](DYLIBS/libETLSAHDynamic.dylib.md)
- [/usr/lib/libMemoryResourceException.dylib](DYLIBS/libMemoryResourceException.dylib.md)
- [/usr/lib/libMobileGestalt.dylib](DYLIBS/libMobileGestalt.dylib.md)
- [/usr/lib/libQMIParserDynamic.dylib](DYLIBS/libQMIParserDynamic.dylib.md)
- [/usr/lib/libTelephonyBasebandDynamic.dylib](DYLIBS/libTelephonyBasebandDynamic.dylib.md)
- [/usr/lib/libTelephonyCapabilities.dylib](DYLIBS/libTelephonyCapabilities.dylib.md)
- [/usr/lib/libTelephonyDebugDynamic.dylib](DYLIBS/libTelephonyDebugDynamic.dylib.md)
- [/usr/lib/libTelephonyUtilDynamic.dylib](DYLIBS/libTelephonyUtilDynamic.dylib.md)
- [/usr/lib/libVinylNonUpdater.dylib](DYLIBS/libVinylNonUpdater.dylib.md)
- [/usr/lib/libchannel.dylib](DYLIBS/libchannel.dylib.md)
- [/usr/lib/libnfshared.dylib](DYLIBS/libnfshared.dylib.md)
- [/usr/lib/librealtime_safety.dylib](DYLIBS/librealtime_safety.dylib.md)
- [/usr/lib/libswiftPrespecialized.dylib](DYLIBS/libswiftPrespecialized.dylib.md)
- [/usr/lib/swift/libswiftAccelerate.dylib](DYLIBS/libswiftAccelerate.dylib.md)
- [/usr/lib/swift/libswiftNaturalLanguage.dylib](DYLIBS/libswiftNaturalLanguage.dylib.md)
- [/usr/lib/swift/libswiftSpatial.dylib](DYLIBS/libswiftSpatial.dylib.md)
- [/usr/lib/swift/libswiftXPC.dylib](DYLIBS/libswiftXPC.dylib.md)
- [/usr/lib/updaters/libVinylUpdater.dylib](DYLIBS/libVinylUpdater.dylib.md)

</details>

### Feature Flags

#### 🆕 NEW (3)

<details>
  <summary><i>View New</i></summary>

#### Urchin.plist

>  `Domain/Urchin.plist`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>urchin</key>
	<dict>
		<key>Enabled</key>
		<true/>
	</dict>
</dict>
</plist>

```
#### ConditionalEngine.plist

>  `Domain/ConditionalEngine.plist`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict/>
</plist>

```
#### GroupKit.plist

>  `Domain/GroupKit.plist`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>FamilyShadow</key>
	<dict>
		<key>DevelopmentPhase</key>
		<string>FeatureComplete</string>
	</dict>
	<key>GroupKitEnabled</key>
	<dict>
		<key>Enabled</key>
		<true/>
	</dict>
	<key>MetadataEnabled</key>
	<dict>
		<key>Enabled</key>
		<true/>
	</dict>
</dict>
</plist>

```

</details>

#### ⬆️ Updated (1)

<details>
  <summary><i>View Updated</i></summary>

#### GlobalDisclosures.plist

>  `GlobalDisclosures.plist`

```diff

 		<key>Disclosed</key>
 		<true/>
 	</dict>
+	<key>11e63eaa-996d-0737-127c-a517dba215e5</key>
+	<dict>
+		<key>Disclosed</key>
+		<true/>
+	</dict>
 	<key>129c9f8f-2dee-4977-5a6e-44aa3830d897</key>
 	<dict>
 		<key>Disclosed</key>

 		<key>Disclosed</key>
 		<true/>
 	</dict>
+	<key>1b3196a9-6a20-4559-60fd-bb3743219ab3</key>
+	<dict>
+		<key>Disclosed</key>
+		<true/>
+	</dict>
 	<key>2298f8e4-f510-4776-b2c1-a85ea314b1f8</key>
 	<dict>
 		<key>Disclosed</key>

```


</details>

## EOF
