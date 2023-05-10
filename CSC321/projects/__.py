if rdr.auth(rdr.AUTHENT1A, 9, key, raw_uid) == rdr.OK:
                            stat = rdr.write(9, byte_integer_data)
                            rdr.stop_crypto1()

                            if stat == rdr.OK:
                                print("Integer data written to card")
                            else:
                                print("Failed to write integer data to card")
                        else:
                            print("Authentication error")