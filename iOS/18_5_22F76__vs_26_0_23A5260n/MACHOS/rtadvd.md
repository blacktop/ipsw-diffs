## rtadvd

> `/usr/sbin/rtadvd`

```diff

-705.100.5.0.0
-  __TEXT.__text: 0x715c
+521.0.0.0.0
+  __TEXT.__text: 0x7668
   __TEXT.__auth_stubs: 0x3e0
-  __TEXT.__cstring: 0x2452
+  __TEXT.__cstring: 0x25b3
   __TEXT.__oslogstring: 0x1e
   __TEXT.__const: 0xc0
-  __TEXT.__unwind_info: 0x118
+  __TEXT.__unwind_info: 0x120
   __DATA_CONST.__auth_got: 0x1f0
   __DATA_CONST.__got: 0x30
   __DATA_CONST.__const: 0x30

   __DATA.__common: 0x114
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libutil.dylib
-  UUID: FE4B8281-A6AD-3B30-BA7B-C0AC41A8B89F
+  UUID: 0ED86F9F-16E4-3D16-B9DE-3BFB462AA0C4
   Functions: 58
-  Symbols:   173
-  CStrings:  309
+  Symbols:   70
+  CStrings:  327
 
Symbols:
+ radr://5614542
- _RM
- _TIMEVAL_ADD
- _TIMEVAL_SUB
- _accept_rr
- _agetent
- _agetflag
- _agetnum
- _agetstr
- _anamatch
- _anchktc
- _conffile
- _delete_prefix
- _dflag
- _do_die
- _do_dump
- _dumpfilename
- _encode_domain
- _find_prefix
- _fp
- _get_addr
- _get_ifam_ifindex
- _get_ifm_flags
- _get_ifm_ifindex
- _get_interface_entry
- _get_next_msg
- _get_prefix
- _get_prefixlen
- _get_rtm_ifindex
- _getconfig
- _getent
- _hopcount
- _if_getflags
- _if_getmtu
- _if_indextorainfo
- _if_nametosdl
- _ifblock
- _ifblock_size
- _ifilist
- _in6a_site_allrouters
- _init_iflist
- _invalidate_prefix
- _lladdropt_fill
- _lladdropt_length
- _main
- _make_packet
- _make_prefix
- _makeentry
- _mcastif
- _nd6_options
- _ndopt_flags
- _pfh
- _pidfilename
- _prefix_check
- _prefix_match
- _prefix_timeout
- _prefixlen
- _ra_output
- _ra_timeout
- _ra_timer_update
- _ralist
- _rcvcmsgbuf
- _rcvfrom
- _rcviov
- _rcvmhdr
- _remotefile
- _rr_input
- _rrcmd2pco
- _rro
- _rtadvdLog
- _rtadvdLogger
- _rtadvd_add_timer
- _rtadvd_check_timer
- _rtadvd_dump_file
- _rtadvd_remove_timer
- _rtadvd_set_dump_file
- _rtadvd_set_timer
- _rtadvd_timer_init
- _rtadvd_timer_rest
- _rtmsg_len
- _rtmsg_type
- _rtpref_str
- _rtsock
- _s
- _set_die
- _set_short_delay
- _sflag
- _sin6_allnodes
- _sndcmsgbuf
- _sndiov
- _sndmhdr
- _so_traffic_class
- _sock
- _tbuf
- _timer_head
- _tm_max
- _tskip
- _update_prefix
- ether_str.hbuf
- getconfig.forwarding
- rtadvdLog.cold.1
- rtadvd_check_timer.returnval
- rtadvd_timer_rest.now
- rtadvd_timer_rest.returnval
- sock_open.answer
CStrings:
+ " "
+ "bad ipv6 address '%s'"
+ "dnr entry %d len %d w/ padding %d"
+ "dnr lifetime '%d'"
+ "dnr service priority '%hu'"
+ "dnraddrs"
+ "dnradn"
+ "dnrentries"
+ "dnrlifetime"
+ "dnrsvcparams"
+ "dnrsvcpriority"
+ "need at least 1 encrypted DNS server addr per DNR entry"
+ "not a valid lifetime %lld"
+ "read addr '%s'"
+ "read addrs str '%s'"
+ "read adn '%s'"
+ "read service parameters '%s'"
+ "reading %d dnr entries"

```
