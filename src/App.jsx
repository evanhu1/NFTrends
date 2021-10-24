import React, { useState } from 'react';
import Rankings from './Rankings';
import Info from './Info';
import { Typography, AppBar, Card, CardActions, CardContent, CardMedia, CssBaseline, Grid, Toolbar, Container, createMuiTheme, ThemeProvider } from '@mui/material';
import AttachMoneyIcon from '@mui/icons-material/AttachMoney';
import Item from '@mui/material/Grid';
import { dark } from '@mui/material/styles/createPalette';
const theme = createMuiTheme({
    typography: {
    fontFamily: [
        'Dosis',
    ],
    fontWeight: '700',
    },
    palette: {
        type: 'dark',
        primary: {
          main: '#44267D',
        },
        secondary: {
          main: '#f50057',
        },
        background: {
          default: '#231A4C',
          paper: '#44267D',
        },
      },
});

function App () {
    const [selectedID, setSelectedID] = useState('no-id');
    return (
        <>
        <ThemeProvider theme={theme}>
            <CssBaseline />
            <AppBar position = "relative">
                <Toolbar color = "primary">
                    <AttachMoneyIcon sx={{fontSize: '2rem'}}/>
                    <Typography sx={{fontSize: '2rem'}}>
                        NFTracker
                    </Typography>

                </Toolbar>
            </AppBar>
            <main>
                <div>

                    <Grid container spacing = {4}>
                        <Grid item xs = {6} align = "center">

                            <Item xs = {8}>
                            
                            <Rankings setSelectedID={setSelectedID}/>
                            
                            </Item>
                        </Grid>
                        <Grid item xs = {6}>
                            <Item xs ={10}>
                                <Info selectedID={selectedID} />
                            </Item>
                        </Grid>
                    </Grid> 
                </div>
            </main>

        </ThemeProvider>
        </>
    );
}
export default App;