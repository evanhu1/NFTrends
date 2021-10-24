import React, { Component, useContext } from 'react';
import Paper from '@mui/material/Paper';
import Item from '@mui/material/Stack';
import Stack from '@mui/material/Stack';
import Typography from '@mui/material/Typography';
import Box from '@mui/material/Box';
import Grid from '@mui/material/Grid';
import { Container } from '@mui/material';

import InfiniteScroll from "react-infinite-scroll-component";

export default function Info({selectedID}) {
    const id = selectedID['name'];
    const rank = selectedID['rank'];
    const count = selectedID['tweets'];
    const imgUrl = selectedID['imgUrl'];
    const desc = selectedID['desc'];
        if (selectedID == 'no-id') {
            return(
                <Typography sx={{fontSize: '2rem', marginTop: '20%'}} color ='white'>Select an NFT to see more info!</Typography>
            );
        }
        else {

        
        return(
            <Container onClick={()=>console.log(selectedID)} style={{ marginTop: '10%'}}>
            <Paper sx={{width: '100%', maxHeight: 7/10, justifyContent: 'center'}}>
              <Stack
                direction="column"
                justifyContent="center"
                alignItems="stretch"
                spacing={2}>
                    <Item>
                        
                            <Grid container spacing = {3}>
                                <Grid item xs = {6}>
                                <Container style={{ marginLeft: '5%', marginTop:'5%'}}>
                                <Typography sx={{fontSize: '3rem'}} color="white">
                                    {id}
                                </Typography>
                                    <Typography  sx={{fontSize: '1rem'}}color="white">
                                        #{rank} Trending NFT
                                    </Typography>
                                    <Typography sx={{fontSize: '1rem'}} color = "white">
                                        {count} Tweets about {} today
                                    </Typography>
                                </Container>
                                </Grid>
                                <Grid item xs = {6}>
                                    <Container style={{alignItems:'center', justifyContent:'center'}}>
                                    <img src={imgUrl}/>
                                    </Container>
                                </Grid>
                            </Grid>  
                        
                    </Item>
                        <Container>
                            <Typography sx={{fontSize: '1rem'}} align='left' color="white" paragraph>
                                {desc}
                            </Typography>
                        </Container>
                    <Item>

                    </Item>

                    {/* <Item>
                        <Container>
                            <Typography sx={{fontSize:'2rem'}} align='left' color='white' >
                                Tweets About {id}
                            </Typography>
                            <InfiniteScroll
                            dataLength={this.state.items.length}
                            next={this.fetchMoreData}
                            hasMore={true}
                            loader={<h4>Loading...</h4>}
                            >
                            {this.state.items.map((i, index) => (
                                <Container style={{backgroundColor:'white'}}>
                                    <Typography>
                                        {index}
                                    </Typography>
                                </Container>
                            ))}
                            </InfiniteScroll>
                        </Container>
                        <Container>

                        </Container>

                    </Item> */}
              </Stack>
          </Paper>
          </Container> 
        );
      }
    }