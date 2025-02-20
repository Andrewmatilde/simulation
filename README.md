TcpAdvancedStat struct {
	// The algorithm used to determine the timeout value used for
	// retransmitting unacknowledged octets, ref: RFC2698, default 1
	RtoAlgorithm uint64
	// The minimum value permitted by a TCP implementation for the
	// retransmission timeout, measured in milliseconds, default 200ms
	RtoMin uint64
	// The maximum value permitted by a TCP implementation for the
	// retransmission timeout, measured in milliseconds, default 120s
	RtoMax uint64
	// The limit on the total number of TCP connections the entity
	// can support., default -1, i.e. infinity
	MaxConn int64

	// The number of times TCP connections have made a direct
	// transition to the SYN-SENT state from the CLOSED state.
	ActiveOpens uint64
	// The number of times TCP connections have made a direct
	// transition to the SYN-RCVD state from the LISTEN state.
	PassiveOpens uint64
	// The number of times TCP connections have made a direct
	// transition to the CLOSED state from either the SYN-SENT
	// state or the SYN-RCVD state, plus the number of times TCP
	// connections have made a direct transition to the LISTEN
	// state from the SYN-RCVD state.
	AttemptFails uint64
	// The number of times TCP connections have made a direct
	// transition to the CLOSED state from either the ESTABLISHED
	// state or the CLOSE-WAIT state.
	EstabResets uint64
	// The number of TCP connections for which the current state
	// is either ESTABLISHED or CLOSE- WAIT.
	CurrEstab uint64

	// The total number of segments received, including those
	// received in error.
	InSegs uint64
	// The total number of segments sent, including those on
	// current connections but excluding those containing only
	// retransmitted octets.
	OutSegs uint64
	// The total number of segments retransmitted - that is, the
	// number of TCP segments transmitted containing one or more
	// previously transmitted octets.
	RetransSegs uint64
	// The total number of segments received in error (e.g., bad
	// TCP checksums).
	InErrs uint64
	// The number of TCP segments sent containing the RST flag.
	OutRsts uint64
	// The number of IP Packets with checksum errors
	InCsumErrors uint64
	// The number of resets received for embryonic SYN_RECV sockets
	EmbryonicRsts uint64

	// The number of SYN cookies sent
	SyncookiesSent uint64
	// The number of SYN cookies received
	SyncookiesRecv uint64
	// The number of invalid SYN cookies received
	SyncookiesFailed uint64

	// The number of packets pruned from receive queue because of socket buffer overrun
	PruneCalled uint64
	// The number of packets pruned from receive queue
	RcvPruned uint64
	// The number of packets dropped from out-of-order queue because of socket buffer overrun
	OfoPruned uint64
	// The number of ICMP packets dropped because they were out-of-window
	OutOfWindowIcmps uint64
	// The number of ICMP packets dropped because socket was locked
	LockDroppedIcmps uint64

	// The number of TCP sockets finished time wait in fast timer
	TW uint64
	// The number of time wait sockets recycled by time stamp
	TWRecycled uint64
	// The number of TCP sockets finished time wait in slow timer
	TWKilled uint64
	// counter, if no more mem for TIME-WAIT struct, +1
	TCPTimeWaitOverflow uint64

	// The number of RTO timer first timeout times
	TCPTimeouts uint64
	// The number of fake timeouts detected by F-RTO
	TCPSpuriousRTOs uint64
	// The number of send Tail Loss Probe (TLP) times by Probe Timeout(PTO)
	TCPLossProbes uint64
	// The number of recovery times by TLP
	TCPLossProbeRecovery uint64
	// The number of RTO failed times when in Recovery state, and remote end has no sack
	TCPRenoRecoveryFail uint64
	// The number of RTO failed times when in Recovery state, and remote end has sack
	TCPSackRecoveryFail uint64
	// The number of RTO failed times when in TCP_CA_Disorder state, and remote end has no sack
	TCPRenoFailures uint64
	// The number of RTO failed times when in TCP_CA_Disorder state, and remote end has sack
	TCPSackFailures uint64
	// The number of RTO failed times when in TCP_CA_Loss state,
	TCPLossFailures uint64

	// The number of delayed acks sent
	DelayedACKs uint64
	// The number of delayed acks further delayed because of locked socket
	DelayedACKLocked uint64
	// The number of quick ack mode was activated times
	DelayedACKLost uint64
	// The number of times the listen queue of a socket overflowed
	ListenOverflows uint64
	// The number of SYNs to LISTEN sockets dropped
	ListenDrops uint64
	// The number of packet headers predicted
	TCPHPHits uint64
	// The number of acknowledgments not containing data payload received
	TCPPureAcks uint64
	// The number of predicted acknowledgments
	TCPHPAcks uint64
	// The number of times recovered from packet loss due to fast retransmit
	TCPRenoRecovery uint64
	// The number of SACK retransmits failed
	TCPSackRecovery uint64
	// The number of bad SACK blocks received
	TCPSACKReneging uint64
	// The number of detected reordering times using FACK
	TCPFACKReorder uint64
	// The number of detected reordering times using SACK
	TCPSACKReorder uint64
	// The number of detected reordering times using Reno
	TCPRenoReorder uint64
	// The number of detected reordering times using time stamp
	TCPTSReorder uint64
	// The number of congestion windows fully recovered without slow start
	TCPFullUndo uint64
	// The number of congestion windows partially recovered using Hoe heuristic
	TCPPartialUndo uint64
	// The number of congestion windows recovered without slow start by DSACK
	TCPDSACKUndo uint64
	// The number of congestion windows recovered without slow start after partial ack
	TCPLossUndo uint64

	// The number of fast retransmits
	TCPFastRetrans uint64
	// The number of retransmits in slow start
	TCPSlowStartRetrans uint64
	// The number of retransmits lost
	TCPLostRetransmit uint64
	// The number of retransmits failed, including FastRetrans, SlowStartRetrans
	TCPRetransFail uint64

	// The number of packets collapsed in receive queue due to low socket buffer
	TCPRcvCollapsed uint64
	// The number of DSACKs sent for old packets
	TCPDSACKOldSent uint64
	// The number of DSACKs sent for out of order packets
	TCPDSACKOfoSent uint64
	// The number of DSACKs received
	TCPDSACKRecv uint64
	// The number of DSACKs for out of order packets received
	TCPDSACKOfoRecv uint64
	// The number of connections reset due to unexpected data
	TCPAbortOnData uint64
	// The number of connections reset due to early user close
	TCPAbortOnClose uint64
	// The number of connections aborted due to memory pressure
	TCPAbortOnMemory uint64
	// The number of connections aborted due to timeout
	TCPAbortOnTimeout uint64
	// The number of connections aborted after user close in linger timeout
	TCPAbortOnLinger uint64
	// The number of times unable to send RST due to no memory
	TCPAbortFailed uint64
	// The number of TCP ran low on memory times
	TCPMemoryPressures uint64
	// The number of TCP cumulative duration of
	// memory pressure events, by ms
	TCPMemoryPressuresChrono uint64
	// The number of SACKs discard
	TCPSACKDiscard uint64
	// The number of DSACKs ignore old
	TCPDSACKIgnoredOld uint64
	// The number of DSACKs ignore no undo
	TCPDSACKIgnoredNoUndo uint64

	// The number of MD5 not found
	TCPMD5NotFound uint64
	// The number of MD5 unexpected
	TCPMD5Unexpected uint64
	// The number of MD5 failed
	TCPMD5Failure uint64
	// The number of Sack shifted
	TCPSackShifted uint64
	// The number of Sack merged
	TCPSackMerged uint64
	// The number of Sack shift fall back
	TCPSackShiftFallback uint64
	// The number of Backlog drop
	TCPBacklogDrop uint64
	// The number of PFmemalloc drop
	PFMemallocDrop uint64
	// The number of memalloc drop
	TCPMinTTLDrop uint64
	// The number of DeferAccept drop
	TCPDeferAcceptDrop uint64
	// The number of IP reverse path filter
	IPReversePathFilter uint64

	// The number of request full do cookies
	TCPReqQFullDoCookies uint64
	// The number of request full drop
	TCPReqQFullDrop uint64

	// number of successful outbound TFO connections
	TCPFastOpenActive uint64
	// number of SYN-ACK packets received that did not acknowledge data
	// sent in the SYN packet and caused a retransmissions without SYN data.
	TCPFastOpenActiveFail uint64
	// number of successful inbound TFO connections
	TCPFastOpenPassive uint64
	// number of inbound SYN packets with TFO cookie that was invalid
	TCPFastOpenPassiveFail uint64
	// number of inbound SYN packets that will have TFO disabled because
	// the socket has exceeded the max queue length
	TCPFastOpenListenOverflow uint64
	// number of inbound SYN packets requesting TFO with TFO set but no cookie
	TCPFastOpenCookieReqd uint64

	// number of SYN and SYN/ACK retransmits to break down retransmissions
	// into SYN, fast-retransmits, timeout retransmits, etc.
	TCPSynRetrans uint64
	// number of outgoing packets with original data
	// (excluding retransmission but including data-in-SYN).
	TCPOrigDataSent uint64

	// The number of active connections rejected because of time stamp
	PAWSActive uint64
	// The number of packetes rejected in established connections because of timestamp
	PAWSEstab uint64
}